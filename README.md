# JPMC-tech-task-1-py3
JPMorgan Chase Software Engineering virtual internship task -1

I am doing virtual internship on JPMorgan Chase Software Engineering for that purpose i created this repo and i am going to share how finsish my task that was given by JPMorgan Chase Software Engineering

before going to task i like to share how i get this internship.

I get the internship on this website insidesherpa <a href="https://www.insidesherpa.com/"> click here</a>
other than JPMorgan Chase Software Engineering lot's of company offer free virtual internship including Microsoft,......


This repo for the task 1

<h3>Task1 </h3>

To know more About Task1 <a hre="https://www.insidesherpa.com/modules/R5iK7HMxJGBgaSbvk/gtAhtcvke9AFCzqME">Click Here</a>

Here is the background information on our task

we’ve been asked to assist with some development to add a chart to a trader’s dashboard allowing them to better identify under/over-valued stocks.

The trader would like to be able to monitor two historically correlated stocks and be able to visualize when the correlation between the two weakens (i.e. one stock moves proportionally more than the historical correlation would imply). This could indicate a potential trade strategy to simultaneously buy the relatively underperforming stock and sell the relatively outperforming stock. Assuming the two prices subsequently converge, the trade should be profitable.

Most data visualization for our traders is built on JPMorgan Chase's Perspective data visualization software, which is now open source.

Before implementing this request using perspective, first you’ll need to interface with the relevant financial data feed and make the necessary adjustments to facilitate the monitoring of potential trade opportunities.

* Understanding the finance and trading part is not required.

* Being familiar with python scripting language and command line basics is not required as you will be guided in this exercise


For the first module of this project will need you to accomplish the following:
<hr>
1.Set up your system by downloading the necessary repository, files, tools and dependencies<br/>
2.Fix the broken client datafeed script in the repository by making the required adjustments to it.<br/>
3.Generate a patch file of the changes you made<br/>
4.Bonus task: Add unit tests in the test script in the repository.<br/>
<hr>
<h4>Step1:Set up your system </h4>
 how to setup your enviroment for this task <a href="https://insidesherpa.s3.amazonaws.com/vinternships/companyassets/Sj7temL583QAYpHXD/setup_devenv_m1_v6.pdf" >Click Here</a> <br/>
 <hr>
 <h4>Step2:Fixing the broken clinet datafeed script<h4>
 
 Before fixing the client code we need to know what the code is actually doing there is 3 python file in the task
 <ol>
      <li>Server3.py</li>
      <li>Client3.py</li>
      <li>Client_test.py</li>
 </ol>
 so let's find what the file is doing <br/>
 <ol>
    <li>Server3.py</li>
        This program is used to serve a stack market data to client by using HttpServer . It read the data from the excel file (test.excel) and send the data to 
        client3.py to knower read the source code<br/>
     <li>client3.py</li>
          This program  get the data from server3.py and calculate the trade price and ratio of two stack price.<br/>
          Before debug this program we need to Know little bit about stack market (not necessary) so it will easy for us to debug
                  <ol>
                  <li>1.Stack market</li>
                  First we need to know little bit about stack market for that i suggest some source below 
                  <li>2.bid price and ask price <li>
                  second we need to know about bid and ask in sharemarket. <br/>
                  <h2>bid</h2>
                  bid is the highest price an invester will to pay for the share 
                  <h2>ask</h2>
                  ask is the lowset price shareholder is willing to pay on shares
                  if you still dont get it read this example<br/>
                  let consider a apple store he sell the apple for 200 rupess.the customer is ask apple for 160 rupess<br/>
                  so the amount said by owner(200) is ask price<br/>
                  the amount said by customer(160) is bid price<br/>

