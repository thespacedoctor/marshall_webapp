# Marshall Webapp

This is the Marshall Webapp for transient surveys and runs in concurrence with the PESSTO Marhsall Engine. 

![The Marshall Webapp](http://i.imgur.com/G2Oro5Q.png)

## API

| Resource  | **Post** | **Get** | **Put** | **Delete** |  
| :------------ | :----------- | :----------- | :----------- | :----------- |
| **/transients** | Add a New Transient  | Bulk Get Transient Info  | Bulk Change Transients  | Not Allowed  |
| **/transients/\<elementId\>**     | Add a New Observation (e.g. classification)  | Get Info for Single Transient  | Change something about the transient (list, pi ...)  | Not Allowed  |
| **/transients/comments**     | Not Allowed  | tbd  | Not Allowed  | Not Allowed  |
| **/transients/\<elementId\>/comments**     | tbd  | Post a new comment for transient  | tbd  | tbd  |
| **/transients/lightcurves**     | Not Allowed  | Not Allowed  | Not Allowed  | Not Allowed  |
| **/transients/\<elementId\>/lightcurves**     | Not Allowed  | Get the lightcurve data for transient  | Not Allowed  | Not Allowed  |
| **/transients/\<elementId\>/obs**     | Not Allowed  | Get the current NTT OB for the transient  | Not Allowed  | Not Allowed  |
| **/transients/search**     | Not Allowed  | Search Transients  | Not Allowed  | Not Allowed  |   |
| **/stats**     | Not Allowed  | Get HTML stats page  | Not Allowed  | Not Allowed  |   |
| **/calendars**     | Not Allowed  | Get HTML calendars page  | Not Allowed  | Not Allowed  |   |


| Actions  | **Post** | **Get** | **Put** | **Delete** |  
| :------------ | :----------- | :----------- | :----------- | :----------- |
| **/actions/refresh_sidebar_list_counts** | Not Allowed  | Update Marshall Sidebar Counts  | Not Allowed  | Not Allowed  |



