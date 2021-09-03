This is a Codeforces bot.
It helps you download all the problem statements and input-output of a contest.

HOW TO USE THIS BOT:
1. install python3 on your pc
2. get the url of the codeforces contest(ex : https://codeforces.com/contest/1411 )
3. run this code and give this url as a system argument(ex : " python3 cf.py https://codeforces.com/contest/1411 " )
4. 


It will make a folder in your working directory (directory in which you run the script), and inside that folder it will create subfolders for each problem.
It also makes a shell script to run c++ code.

HOW TO RUN YOUR C++ CODE:(For Linux users only)
1. navigate to the folder where all the files are present
2. run this command to give permission to the shell script( "chmod +x cp.sh" )
3. run "./run contest_id problem_number", for ex "./run 1411 A" 
    
    Note: 
    1. constest_id is unique number in url of contest, for example in https://codeforces.com/contest/1411 contest code is 1411
    2. problem number is A, B,C etc.
It will compile and execute your code and compare your output with the actual output.