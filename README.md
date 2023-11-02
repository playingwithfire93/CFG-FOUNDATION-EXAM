Section 1: Theory Questions [31 marks]

1.1    What does SDLC stand for? System development life cycle	

   1.2   What exception is thrown when you divide a number by 0?
ZeroDivisionError	

   1.3   What is the git command that moves code from the local repository to the remote repository? 
git push <remote> <branch> (remote is the remote repository we want to move the code to and branch is the branch it the local code comes from)	

   1.4   What does NULL represent in a database?
That the given variable in a database doesn't have a value, that is undefined or unknown. 	   


   1.5   Name 2 responsibilities of the Scrum Master 
-Coaching an mentoring team.
-Conflict Resolution.	

   1.6   Name 2 debugging methods, and when you would use them.
Unit testing -->Unit testing is most useful when you're building your code to check if different sections of your code work as they should. It's really good for finding and solving problems early in the development process.
	  

   1.7   Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. 

An TypeError could arise if the price and cash_given have different types of values, like one is a string and another is a float for example.
You could fix this by converting both variables to int or float in the if statement.
def can_pay(price, cash_given):
   if cash_given >= price:
       return True
   else:
       return False

   1.8    What is git branching? Explain how it is used in Git.

It's a version control system that enables developers to isolate changes, communicate, and work on the same project simultaneously.
1. You first use the command "git branch" to create the branch.
2. Then you use "git checkout <branch name>" to move from main to said branch.
3. Then you use "git commit" to save the changes you made in said branch.
4. When you make sure that you have solved and there's no more issues with the code, you move it back to main with the command "git merge main"
5. The last thing you would do is delete the branches with the command "git branch -d <branch name>"



   1.9  Design a restaurant ordering system. 
           You do not need to write code, but describe a high-level approach: 
⦁	Draw a list of key requirements
⦁	What are your main considerations and problems?
⦁	What components or tools would you potentially use? 

 


	  10 marks
