import time
alarms = {
    u'rowset':
    {u'rows':
     [
         {u'Node': u'WE2O-AIRM4-0100', u'LastOccurrence': 1605469763, u'AlarmDetails': u'Remote site monitoring', u'Severity': 4, u'AdditionalText':
             u' Element is down Element is down 1593147204 1593147204 1593147204   1593147204 WE2O 1/14/13/18  10.127.227.216 53 58 Data Collection Device WE2O-AIRM4-0100 Remote NodeDown Alarm Westell Westell CFWW-AIRMX-0100 Eth 4  Remote site monitoring', u'Summary': u'Element is down', u'NodeAlias': u'WE2O-AIRM4-0100', u'LRDCode': u'WE2O', u'ClearTimestamp': 0},
         {u'Node': u'WE2O-AIRMM-0100', u'LastOccurrence': 1605505763, u'AlarmDetails': u'Remote site monitoring', u'Severity': 3, u'AdditionalText':
          u' Restore point incomplete All child status(es) are abnormal 1593230752 1593230752 1593317180   1593317180 WE2O 1/14/13/18  10.127.227.216 53 58 Data Collection Device WE2O-AIRMM-0100 Remote RestorePoint Alarm Westell Westell CFWW-AIRMX-0100 Eth 4  Remote site monitoring', u'Summary': u'Restore point incomplete', u'NodeAlias': u'WE2O-AIRMM-0100', u'LRDCode': u'WE2O', u'ClearTimestamp': 0},
         {u'Node': u'', u'LastOccurrence': 1593361323, u'AlarmDetails': u'A fuel tank driven by a meas table entry', u'Severity': 4, u'AdditionalText':
             u' LevelPercent is less than 60.0% (1200/2000 L) LevelPercent is less than 60.0% (1200/2000 L) 1589409196 1589409196 1590661740   1590661740 WE2O    53 57 AnalogFuelTank WE2O DayTankFuelSensor MeasTableFuelTank LowFuel Alarm Kentrox Kentrox   A fuel tank driven by a meas table entry', u'Summary': u'LevelPercent is less than 60.0% (1200/2000 L)', u'NodeAlias': u'WE2O DayTankFuelSensor', u'LRDCode': u'WE2O', u'ClearTimestamp': 0},
         {u'Node': u'', u'LastOccurrence': 1593434962, u'AlarmDetails': u'Remote site monitoring', u'Severity': 3, u'AdditionalText': u' Restore point incomplete All child status(es) are abnormal 1593230752 1593230752 1593317180   1593317180 WE2O 1/14/13/18  10.127.227.216 53 58 Data Collection Device WE2O-AIRM9-0100 Remote RestorePoint Alarm Westell Westell CFWW-AIRM9-0100 Eth 4  Remote site monitoring', u'Summary': u'Restore point incomplete', u'NodeAlias': u'WE2O-AIRM9-0100', u'LRDCode': u'WE2O', u'ClearTimestamp': 0}, {u'Node': u'', u'LastOccurrence': 1593434962, u'AlarmDetails': u'Remote site monitoring', u'Severity': 4, u'AdditionalText': u' Element is down Element is down 1593147204 1593147204 1593147204   1593147204 WE2O 1/14/13/18  10.127.227.216 53 58 Data Collection Device WE2O-AIRM9-0100 Remote NodeDown Alarm Westell Westell CFWW-AIRMX-0100 Eth 4  Remote site monitoring', u'Summary': u'Element is down', u'NodeAlias': u'WE2O-AIRM9-0100', u'LRDCode': u'WE2O', u'ClearTimestamp': 0}, {u'Node': u'WE2O-AIRM4-0100', u'LastOccurrence': 1593435132, u'AlarmDetails': u'Remote site monitoring', u'Severity': 3, u'AdditionalText': u' Restore point incomplete All child status(es) are abnormal 1593230752 1593230752 1593317180   1593317180 WE2O 1/14/13/18  10.127.227.216 53 58 Data Collection Device WE2O-AIRM4-0100 Remote RestorePoint Alarm Westell Westell CFWW-AIRM4-0100 Eth 4  Remote site monitoring', u'Summary': u'Restore point incomplete', u'NodeAlias': u'WE2O-AIRM4-0100', u'LRDCode': u'WE2O', u'ClearTimestamp': 0}, {u'Node': u'WE2O-AIRMM-0100', u'LastOccurrence': 1593434708, u'AlarmDetails': u'Remote site monitoring', u'Severity': 4, u'AdditionalText': u' Element is down Element is down 1593147204 1593147204 1593147204   1593147204 WE2O 1/14/13/18  10.127.227.216 53 58 Data Collection Device WE2O-AIRMM-0100 Remote NodeDown Alarm Westell Westell CFWW-AIRMX-0100 Eth 4  Remote site monitoring', u'Summary': u'Element is down', u'NodeAlias': u'WE2O-AIRMM-0100', u'LRDCode': u'WE2O', u'ClearTimestamp': 0}], u'tblname': u'status', u'osname': u'SDAOSR1_B', u'coldesc': [{u'type': u'string', u'name': u'LRDCode', u'size': 7}, {u'type': u'string', u'name': u'Node', u'size': 64}, {u'type': u'string', u'name': u'NodeAlias', u'size': 64}, {u'type': u'string', u'name': u'Summary', u'size': 255}, {u'type': u'integer', u'name': u'Severity', u'size': 4}, {u'type': u'string', u'name': u'AdditionalText', u'size': 4096}, {u'type': u'string', u'name': u'AlarmDetails', u'size': 255}, {u'type': u'utc', u'name': u'LastOccurrence', u'size': 4}, {u'type': u'utc', u'name': u'ClearTimestamp', u'size': 4}], u'affectedRows': 7, u'dbname': u'alerts'}}

print(alarms)
print([x for x in alarms['rowset']['rows'] if (
    x['LastOccurrence']) > time.time() - 21800 * 3])


# alarms = [x for x in alarms if (x['createdDate'] /
#                                 1000) > (time.time() - 3600 * 34)]
# print(time.time())
# print(time.time() - 43200)
# print(alarms)

# print(1605389208659/1000 > 1605462186)
# 1605389208 2020-11-14T21:26:48+00:00 GMT 2020-11-15T08:26:48+11:00 +11
# 1605462186 2020-11-15T17:43:06+00:00 GMT 2020-11-16T04:43:06+11:00 +11
