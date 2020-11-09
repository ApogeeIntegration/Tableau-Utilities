# ParamFlipper

Tableau Extension

## Getting Started


### Prerequisites
- IDE of your choice, [Visual Studio Code](https://code.visualstudio.com/) recommended
- [Git](https://git-scm.com/downloads)


### Setting Up the Development Environment
1. Clone this repository to a location of your choice

    `git clone https://github.com/ApogeeIntegration/Tableau-Utilities.git`
2. Create a new branch for your feature

    `git checkout -b "branch_name"`
3. Set the location of the file location to localhost- uncomment line 11 and comment out line 10 of paramFlipper.trex


### Setup

1. Download Tableau Desktop (use a company License or free trial)
2. Download Chromium version 79 (a very old version of chrome will also work)
3. In your terminal, navigate to the paramFlipper folder of the Tableau-Utilities project and run
    `http-server`
4. In a different terminal, naviage to the bin folder of Tableau (example: C:\Program Files\Tableau\Tableau 2020.3\bin) and start tableau with debugging by running
    `tableau.exe --remote-debugging-port=9000`
5. Add the extension (paramFlipper.trex) to the opened Tableau application
6. Navigate to http://localhost:9000/ in chromium to debug the extension
7. To redeploy the master branch to S3, go to apogee's S3 bucket apogee-tableau-paramflipper, delete contents- excluding assets folder, and reupload new contents
 
## License
This project and the code within is APOGEE Proprietary Information.

## Contributors
* **Jacob Meadows**
* **Andrea Howes** - [github](https://github.com/ashcreek)


## Contact
If you have any questions, please contact Andrea Howes at ahowes@apogeeintegration.com.