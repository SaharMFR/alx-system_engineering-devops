#Outage Postmortem : The Database Disconnect Debacle

###Issue Summary :

**Duration :**
Start Time : December 1, 2023, 2:30 PM (UTC)
End Time : December 1, 2023, 5:00 PM (UTC)

**Impact :**
A simple demo banking system, developed for a class project, experienced a 2.5-hour outage. Users were unable to access account information, leading to confusion and a 15% decrease in project completion progress.

**Root Cause :**
The outage was caused by a misconfiguration in the database connection string during a routine update, resulting in failed queries.

###Timeline :

**Detection :**
December 1, 2023, 2:45 PM (UTC)
Users reported errors when trying to access account information through the banking system.
**Actions Taken :**
Investigated server logs and identified database connection errors.
Initially assumed a server overload and increased resources, which did not resolve the issue.
Escalated the incident to the development team for further investigation.
**Misleading Paths :**
Suspected potential issues with the banking application, exploring coding errors.
Briefly considered network problems but ruled it out with successful ping tests.
**Escalation :**
Escalated the incident to the senior software engineer and the database administrator.
**Resolution :**
Discovered the misconfiguration in the database connection string.
Rolled back the recent update to the previous version and corrected the database connection settings.

###Root Cause and Resolution:

**Root Cause :**
Misconfiguration in the database connection string during a routine update, resulting in failed queries.

**Resolution :**
Rolled back the recent update to the previous version and corrected the database connection settings, restoring functionality to the demo banking system.

###Corrective and Preventative Measures :

**Improvements/Fixes :**
Enhance the deployment checklist to include thorough testing of database connection strings.
Implement automated tests for database connectivity in the continuous integration pipeline.

**Tasks :**
Update documentation with explicit instructions on configuring and testing database connections.
Conduct a post-incident review with the development team to discuss lessons learned and improve response procedures.


In the midst of the banking breakdown, we briefly entertained the idea of introducing a "Manual Ledger Entry" feature, encouraging users to track their transactions with pen and paper. Alas, it was short-lived as we swiftly resolved the issue and brought back the digital convenience to our demo banking system!

###Conclusion :

The Database Disconnect Debacle highlighted the importance of meticulous testing, even in simple projects. By implementing the suggested improvements and tasks, we aim to prevent future disruptions and ensure smooth project development experiences. Keep coding, keep testing!
