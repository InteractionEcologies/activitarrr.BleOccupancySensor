### 2/23
* Goal
 + Fix the OccupancyTracker App bug

* Notes
 + Bug 1
	- After rebuild the system, cannot detect the BleOccupancy Tracker.
    	- change VM ware from NAT to bridged: success
 + Bug 2
 	- Adter pressing update in the AppOccupancyTracker web page, the front-end did not receive the right response
 	- Who will call GetLastReport of BleOccupancyManager.cs?
 		- 

 + Debug Process
 	- Remove the Config file in the Config folder
 	- Rebuid the Driver if needed (e.g., Activitarrr.BleOccupancy)
 	- Rebuild the platform
 	- Start the debugging (Visual Studio)

