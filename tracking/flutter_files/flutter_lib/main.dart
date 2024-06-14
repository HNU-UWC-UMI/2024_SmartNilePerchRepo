import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

import 'package:intl/intl.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: LocationScreen(),
    );
  }
}

class LocationScreen extends StatefulWidget {
  @override
  _LocationScreenState createState() => _LocationScreenState();
}

class _LocationScreenState extends State<LocationScreen> {
  String _locationMessage = "";
  bool _isTracking = false;
  StreamSubscription<Position>? _positionStreamSubscription;
  Timer? _logTimer;

  void _startTracking() async {
    bool serviceEnabled;
    LocationPermission permission;

    serviceEnabled = await Geolocator.isLocationServiceEnabled();
    if (!serviceEnabled) {
      setState(() {
        _locationMessage = "Location services are disabled.";
      });
      return;
    }

    permission = await Geolocator.checkPermission();
    if (permission == LocationPermission.denied) {
      permission = await Geolocator.requestPermission();
      if (permission == LocationPermission.denied) {
        setState(() {
          _locationMessage = "Location permissions are denied.";
        });
        return;
      }
    }

    if (permission == LocationPermission.deniedForever) {
      setState(() {
        _locationMessage = "Location permissions are permanently denied.";
      });
      return;
    }

    setState(() {
      _isTracking = true;
      _locationMessage = "Tracking started.";
    });

    _positionStreamSubscription = Geolocator.getPositionStream().listen((Position position) {
      String timestamp = DateTime.now().toString();
      setState(() {
        _locationMessage = "Lat: ${position.latitude}, Lon: ${position.longitude}\nTime: $timestamp";
      });
    });

    // Start the timer to log data every 20 seconds
    _logTimer = Timer.periodic(Duration(seconds: 20), (Timer timer) async {
      Position position = await Geolocator.getCurrentPosition(desiredAccuracy: LocationAccuracy.high);
      // String timestamp = DateTime.now().toString();
      var formatter = DateFormat('yyyy-MM-dd HH:mm:ss');
      String timestampStr =formatter.format(DateTime.now());
      String targetOBJ = "phone"; // Use "phone" as the target object
      String gpsOrigin = "real"; // Use "real" as the gps origin

      // Prepare the data to be sent
      final data = json.encode({
        'lati': position.latitude,
        'longi': position.longitude,
        'TimeStamp': timestampStr,
        'targetOBJ': targetOBJ,
        'gpsOrigin': gpsOrigin,
      });

      // Send the data via HTTP POST request
      try {
        var response = await http.post(
          Uri.parse('https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/GpsData'),
          headers: {'Content-Type': 'application/json'},
          body: data,
        );

        print(data);

        if (response.statusCode == 200) {
          print('Location data sent successfully.');
        } else {
          print('Failed to send location data.');
        }
      } catch (e) {
        print('Error occurred while sending location data: $e');
      }
    });
  }

  void _stopTracking() {
    if (_positionStreamSubscription != null) {
      _positionStreamSubscription!.cancel();
    }
    if (_logTimer != null) {
      _logTimer!.cancel();
    }
    setState(() {
      _isTracking = false;
      _locationMessage = "Tracking stopped.";
    });
  }

  @override
  void dispose() {
    if (_positionStreamSubscription != null) {
      _positionStreamSubscription!.cancel();
    }
    if (_logTimer != null) {
      _logTimer!.cancel();
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Location Tracker"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Text(_locationMessage),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _isTracking ? null : _startTracking,
              child: Text("Start Tracking"),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: _isTracking ? _stopTracking : null,
              child: Text("Stop Tracking"),
            ),
          ],
        ),
      ),
    );
  }
}







