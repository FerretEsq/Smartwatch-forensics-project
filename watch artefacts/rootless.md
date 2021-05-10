# Notes on testing without root

# Findings
Inside watch storage there is a txt file named "iport_logs". These logs appear to show when the time & date of when the device was turned on & off, upgraded, and whether the upgrade was a success or not.
When inspecting the file tree, there are only 4 directories which arent empty : 
- "/PhoneStorage/Android/data/com.android.watchweather/files/baidu/tempdata"
- "/../../../com.mediatek.watchapp/catch/uil-images"
- "/baidu/tempdata/
The /baidu/tempdata directory has an sqlite database inside it
