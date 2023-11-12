# postmortem

## Objective:
This postmortem aims to analyze the recent incident where our website experienced 500 Internal Server Errors, identify the root causes, and outline action items to prevent similar occurrences in the future.

## Summary of Events:
June 10, 2023, from 2:30 p.m. to 5:00 p.m. (UTC+1), our website experienced an internal server error. The website stopped responding and 80% of users could not access it during this time. The cause of the error was a memory leak on our web application server.

## Timeline:
Juin 10, 2023, 2:30 p.m. to 5:00 p.m. (UTC+1)
* 2:30 PM — the monitoring system detected a surge in 500 Internal Server Errors.
*	2:35 PM — the web operations team was alerted and initiated an investigation.
*	3:45 PM — the team identified the memory leak in the code and began working on a fix.
*	4:30 PM — the team deployed the fix and restarted the web application server.
* 5:00 PM — the website was back online and fully operational.

## Root Cause: 
Our website recently encountered a series of 500 Internal Server Errors, resulting in a degraded user experience and temporary unavailability of services. The root cause of the error was a memory leak on our web application server. A memory leak caused the server to become overloaded and unresponsive, resulting in a full website shutdown.
Misleading Investigation/Debugging Paths:
The team initially assumed that the problem was related to the server configuration and invested valuable time investigating. This delayed determining the true cause of the problem.

## Corrective and Preventative Measures:
To prevent this issue from happening in the future, we decided to take these preventative measures :
*	We will implement daily reviews of the code
*	We will optimize the code to prevent memory leaks
*	We will improve documentation 
*	we will train the operations team to better handle incidents in the future.

