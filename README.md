# Introduction and Targets
small description 2-3 sentences  
Document about Fish-Transportation in Uganda: [link](./doc/Fish%20Transportation%20in%20Uganda.pdf)  
End Presentation: [link](.???)  

Link to Miro-Board: https://miro.com/app/board/uXjVMTfASQ4=/  

## Tasks

create links to UserStories from Project

## Stakeholder

| Role         | Contact        | Expectations      |
|--------------|----------------|-------------------|
| Product Owner| dany.meyer@hnu.de | The need for wireless technologies and tracking systems (architecture) makes a business sense in terms of cold chain management of the container for safety of fish and remote tracking for security of fish. I expect a system as a prototype with which I can demonstrate a digital solution that monitors and evaluates the temperature and position of a box. I would like to experience the creation of the prototype within a week by an agile team.|
| *\<Rolle-2>* | *\<Kontakt-2>* | *\<Erwartung-2>*  |

## Sub-Projects / Team

| Sub-Project/Modul | Team | Names + Responsibility      |  
|--------------|----------------|----------------|
| *\<Example Modul>*  | Team A | Micky Mouse (py-Code), Donald Duck (doc), Gustav Gans (test)|
| Apex-DB  |  Team 4 |*\<Name1, Name2, Name3, Moritz.Gruber (DBAdministration, RESTful-Provider)>*  |
| Apex-Forms  |  Team 4 |*\<Name1, Name2, Name3, Name4>*  |
| IoT-Counter  |  Team 3 |*\<Alexander Schobloch (py-Code, doc), Julia Hosch (py-Code, test), Yusuf Gitta (Requirements, Presentation), Nomonde Bridgette Zama (Requirements, Presentation)>*  |
| IoT-Temperature |  Team 2 |*\<Jenny Gia-Linh Huynh (py-code, grafana, Apex-DB), Isabell Riffel(github documentation), Siyabonga Luvuno Jele(py-code, grafana)=, Isaac Senda(presentation slides)>*  |
| Grafana  |  Team 2 |*\<Siyabonga Luvuno Jele, Jenny Gia-Linh Huynh, Name3, Name4>*  |
| GPS-Flutter-App |  Team 1 |*\<Name1, Name2, Name3, Name4>*  |
| GPS-Map  |  Team 1 |*\<Name1, Name2, Name3, Name4>*  |
| Box Prototyp |  Team 2 / Team 3 |*\<Alexander Schobloch, Julia Hosch, Jenny Gia-Linh Huynh, Siyabonga Jele>*  |

# Systemarchitecture
Picture  
*\<Link a picture>*  

Modules  
*\<Short Description e.g.>*
1. The Module Apex-Backend is used to store data, provide REST interfaces and dialogs for data input and reporting
2. The Module IoT-Counter is used ..
3. The Module IoT-Temp is used ..
4. The Module GPS-App is used ..
5. ...

Interfaces  
*\<Short Description of interfaces>*

## Module Apex-Backend: DB-Model
* *\<Target/Requirement>*
* *\<Interfaces: links to GET + POST + examples of JSON>*
* *\<Concepts: ER-Diagramm>*
* *\<Artifacts: link to ddl>*
* *\<Artifacts: screenShots of Apex-Forms>*
* *\<Access to Apex: link / user /pwd>*

## Module IoT-Counter+Temp (both Teams together)
* *\<Target/Requirement>*
* *\<Interfaces: links to POST>*
* *\<Concepts: Description of Logic + used Hardware>*
* *\<Artifacts: links to py-Code>* [Counter](./raspberry/Counter.py)   [DB_Creation](./raspberry/creating_db_fish_size.py)   [Temp](./raspberry/Temp.py)
* *\<Artifacts: fotos of Box>* [Box](./images/SmartContainer_Box.jpeg) 

## Module GPS
* *\<Target/Requirement>*
* *\<Interfaces: link to GET's + POST + examples of JSON>*
* *\<Concepts: Flutter App, Map>*
* *\<Artifacts: link to Flutter-Project>*
* *\<Artifacts: link to py..>*
* *\<Artifacts: screenShots of..>*
 
## Module Grafana
* *\<Target/Requirement>*
* *\<Interfaces: links to GET>*
* *\<Concepts: which Platform>*
* *\<Artifacts: screenShots Grafana>*



# Links from the Database
| Link         |        |
|--------------|----------------|
| *https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/TEMPERATURE_DATA* | *temp* | 
| *https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/FISHCOUNTER_DATA* | *counter* | 
| *https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/FISHDESC_DATA* | *description* | 
| *https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/GpsData* | *gps* | 
| *https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/INSPECTORREPORT_DATA* | *inspector-form* | 
| *https://jelesiya.grafana.net/d/edondbv483zswc/temperature-dashboard?orgId=1&refresh=5s&from=1718266788853&to=1718288388854* | *Dashboard temperature* |
| *https://jelesiya.grafana.net/d/cdonvamsva9z4a/fishcounter-dashboard?orgId=1&refresh=5s&editIndex=0&from=1718267023970&to=1718288623970* | *Dashboard fishcounter* |


# Planning

| Group         | Mon        | Tue      | Wed   | Thu  | Fri  |
|--------------|----------------|-------------------|-------------|------------|---------|
| 1 | .. | ..  | .. | ..| .. |
| 2 |  Week planning, Issues | Data Base, work with Raspberry Pie   | Connecting with the other Groups, Integration, Testing, Dokumentation, Grafan  | Grafana, Data base, work with group 3 | Presentation |
| 3 | General planning/identifting/defining tools to use/understanding the integration of the the use case | looking at the raspeberry and the different sensors to use that will be applicable for counting and measuring the fish/created a simulation environment to use the scale to define weight of the fish. The simualation code worked but we change the plan to use a infared sensor | Integrating count system with temperature system | Database implemention and connection| Building the system and presentation |
| 4 |  General Planning procedures / increment for group and the whole project | Prepraring a Prototyp for the UI using MIRO / Deciding on a DBMS + First Considerations about InfluxDB / Firebase and finally Oracle Apex + Establishing first ER & ERR_Models| Getting started on Oracle Apex / Table Creation / REST-API | Integrating the other Groups in the DB / Refining Processes / Integrating the general Form for the Insepctor / Creation of UI-Interface using Oracle Apex| Final Refinements before the Presentation (Integration of the optimized Inspector_Report + Preparation Process for the Final_Presentation |



*\<Problems/Risks>*
