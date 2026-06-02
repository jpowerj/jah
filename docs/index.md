---
title: Autohinter Frequently Asked Questions
icon: material/frequently-asked-questions
---

**Overivew:** Assignments will be **manually graded**, and these grades will be entered on both Canvas and Google Classroom. To **submit** each assignment, all you need to do is **save** your Colab notebook: when the late-submission period for each assignment ends, we will take your most-recently-updated notebook files and grade these as your submission. See the following sections for Frequently Asked Questions (FAQs) about the **hint reports** you can automatically request for each assignment (by clicking the **"Get Feedback"** button at the bottom of your notebook).

## Are the results in the autohinter report the same my grade on an assignment?

**No!**

The **autohinter report** is there for the sake of *learning*: the goal is to enable you to *try* different approaches to solving a problem, then receive *instant feedback* on whether your approach has brought you closer-to or further-from the solution.

Your ultimate **recorded grade** for an assignment is based on **human, manual grading** of the assignment, so that we can take into account things like:

* Alternative ways to arrive at the solution that we (as instructors) did not foresee when making the autohinting code for that question
* Contextual details that you can **write into** your responses (using Colab's "Add Comment" feature on the response cell), to clarify why you chose one response over another and/or why you are confused about something in the autohinter report

## Why am I seeing a "500: Internal Server Error" message when I request an autohinter report?

This error could have many causes, since it just means that "something has occurred within the server code that led to a crash".

However, one of the most common reasons for this, and the simplest to fix, is that <strong>the autohinter code "detects" your response cells</strong> for a given question like (say) Q3.2 by <strong>finding a code cell with <code># @title Q3.2-response</code> as its first line</strong>. Although these are the default first lines in each code cell when the Colab notebooks are distributed, you may have inadvertently changed the first line in a given response cell while working on the assignment.

A simple way to detect and fix where this might be happening in your code is to open the <strong>Table of Contents</strong> view on the left side of the Colab interface: any code cells that start with <code># @title</code> will be "registered" in Colab's Table of Contents, so that in this Table of Contents listing you should see e.g. Question 1.1 followed by an indented "Q1.1-response", Question 1.2 followed by an indented "Q1.2-response" listing, and so on. If one of these "QX.X-response" entries is missing (for example, if the Table of Contents skips directly from "Question 1.1" to "Question 1.2"), find the relevant code cell and then re-add <code># @title Q1.1-response</code> as its first line.

## Why am I seeing a "404: Resource Not Found" message when I request an autohinter report?

Here, the first thing to check is the **URL** of the server that the submission cell is using: Previous versions of the class used a National Science Foundation "Jetstream" server, but this semester we are using a (...personally funded) Google Cloud Run setup.

So, this just means:

If you see the older URL:
    
```
http://jag.soc240036.projects.jetstream-cloud.org:5000/submit
```
    
Replace it with the new Google Cloud Run URL:
    
```
https://jah-submit-83645199100.us-east4.run.app/
```

If you replace the URL and now get a 500 error, see the above entry. If you replace the URL and <i>still</i> get a 404 error, this means that the server is fully <strong>down</strong>, meaning that this error is happening <i>before</i> your notebook is even able to reach the server. In this case, the problem is most likely something like a server crash rather than any issue within your notebook, so please contact Jeff at <a href='mailto:jj1088@georgetown.edu' target='_blank'><code>jj1088@georgetown.edu</code></a> if you encounter this 404 error.
