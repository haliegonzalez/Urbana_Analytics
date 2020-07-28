# Urbana Analysis
Data Analysis of Urbana, IL and Champaign County

## Some notes about Jupyter Notebook
### What is Jupyter Notebook? How do I use it?
Jupyter Notebook is a program that allows you to easily write, run, and share Python code. Jupyter Notebooks are saved in .ipynb files that can be opened if you install Anaconda. A useful link to learning how to download Anaconda for Jupyter Notebook is here: <https://wiki.harvard.edu/confluence/display/USERDOCS/Anaconda+Python+Installation+and+Jupyter+Notebook>. You need Anaconda if you wish to use Jupyter Notebook. Another useful link for learning how to use Jupyter Notebook and what the interface looks like is here: <https://www.dataquest.io/blog/jupyter-notebook-tutorial/>. Jupyter Notebook files can also be saved as .py files (which this repository also has) which can be directly run in a terminal. If you don't want to download Anaconda and just view the notebook, you can go to <https://nbviewer.jupyter.org/> and copy and paste the link of the .ipynb notebook in this GitHub repository. Nbviewer has instructions on what link to copy and paste. For example, if I want to view the Demographic, Economic, Transportation, and Health Conditions notebook, first navigate to the .ipynb file in this repository, copy the url, go to nbviewer.jupyter.org, and paste the link which in this case is "https://github.com/haliegonzalez/Urbana_Analytics/blob/master/Demographic%2C%20Economic%2C%20Transportation%2C%20and%20Health%20Conditions.ipynb".

### How do I clone this repository?
If you plan to run the notebooks in this repository, you need to download the entire Urbana_Analytics repository so that you have the data. If the file path name doesn't match or you don't have the data available, then the notebook simply won't run. To do this, you can go to my GitHub at <https://github.com/haliegonzalez/Urbana_Analytics> (where you presumably already are) and git clone this repository. To git clone, click the green button that says `Code`, copy the URL shown, and go to your terminal and type `git clone https://github.com/haliegonzalez/Urbana_Analytics.git`. If you aren't comfortable with this, you can also just download the zip file. Again, keep in mind that you will likely need to change the file paths seen in the notebooks when I import the datasets. This is because I used the file paths on my local computer which are likely different than the ones you will find on your local computer. This would involve, for example, changing "/Users/haliegonzalez" to whatever your file path is. 


### How do I run and write code in Jupyter Notebook?
If you have Jupyter Notebook you can run code in the Jupyter Notebook workspace. To do this, first you must download Anaconda as indicated above. Open the Anaconda application, and click `Launch` under Jupyter Notebook. This will open up Jupyter Notebook in your browser. From there, click on whatever folder your notebook is saved under. If you cloned this repository (instructions below), you should see it either in the Downloads folder or as its own listed folder. From there, you just click into the .ipynb notebook and you will be in the Jupyter Notebook workspace!

To create a cell for coding you can click the `+` in the top left of the workspace. This will create a code cell. Make sure that the drop down box at the top of the workspace under "Widgets" and "Help" says `Code` and not the following: `Markdown`, `Raw NBConvert`, or `Heading`. Once you have a cell open, you can go ahead and start writing your code! To run the code, do `shift`-`enter` and it will run the cell. Alternatively, you can go to the top left of the Jupyter Notebook workspace, click `Cell`, and choose whichever run type you are interested in. `Run cells` will run the particular cell you are working in. You can also choose to run all, run all above, run all below, etc.

To create a cell with written text rather than code, go to the drop down box at the top of the workspace under "Widgets" and "Help" and change the type from `Code` to `Markdown`. You will now be working in a Markdown cell that uses LaTex documentation. LaTex is a commonly used mathtype that makes it incredibly easy to type up elegant looking mathtype. If you wish to have incredibly large, bold text, do the following: '# Word'. If you wish to have slightly less large, bold text, put two #'s. Adding more #'s will decrease the size of the font up to 4 #'s. You can experiment with what will happen if you use more than 4 #'s! To write in normal font, just write as you normally would in a text cell. When you are done writing text, do `shift`-`enter` and you will have the text produced for you that looks just like the text written here. To edit the text after doing `shift`-`enter` you can double click in the cell.



Good luck!
