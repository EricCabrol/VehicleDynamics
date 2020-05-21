# Fundamentals of vehicle dynamics and modelling

Book published in 2019, and first attempt from the writer, [Bruce Minaker](http://www.uwindsor.ca/engineering/mame/321/dr-b-minaker), associate professor at the university of Windsor. 

![book cover](https://media.wiley.com/product_data/coverImage300/93/11189800/1118980093.jpg)

The [preface](https://books.google.fr/books?id=-HCqDwAAQBAJ&pg=PA1&hl=fr&source=gbs_toc_r&cad=3#v=onepage&q&f=false) explains his intent :
> I have found many texts on  this topic and others that, while providing good relevant coverage, add much more content than necessary. I believe that this level of breadth is not in the  reader's best interest, With many Ieft overwhelmed by the prospect of mastering so much material, and eventually resigning themselves to never finishing.  
> (...)  
> **The book does not aim to be a complete reference, but rather to give a solid foundation while generating enthusiasm in the student reader**

As a result the book is rather short (a little less than 200 pages) ... which results in a high $/page cost :)  

Chapters 
1. Introduction
2. Tire Modelling
3. Longitudinal dynamics
4. Linear dynamic models
5. Full car model
6. Multibody dynamics
7. Mathematics

Most chapters are illustrated with a few numerical examples, and also with problems (no solutions given).

The chapter dedicated to **tire modelling** is very brief (10 pages), almost equation-free (no Magic Formula inside !), it is a  basic introduction to the underlying physics.

**Longitudinal dynamics** deals with acceleration and braking performance, with a focus on load transfer. The optimal brake distribution is very clearly explained. 

**Linear models** are then introduced, starting with the *yaw plane* model for cornering dynamics (often called bicycle model in the literature). The classical first-order system is derived and its applications are illustrated, both for steady-state analysis and for transient behaviour. Stability conditions are discussed, explaining clearly the influence of the front/rear location of the center of gravity. A *truck and trailer* model is also presented.  
For vertical motion, two models are presented : *quarter-car* for suspension analysis, and *bounce-pitch* for vehicle body motion.

A **full-car model** is presented in chapter 5, restricted to bounce, pitch and roll motions (no longitudinal neither lateral equations). The way this chapter is built doesn't seem as obvious as the previous ones. Firstly some pages more heavily loadedof equations and linear algebra, just to conclude that the problem becomes too big to be solved by hand and must be computed numerically. Then only a few lines to comment the results obtained and detail the corresponding modes. Then we get back to more physics with a paragraph about kinematic effects (roll centers, jacking effects ...), but I don't understand the timing. 

Chapter 6 about **Multibody dynamics** becomes more theoretical, explaining how the governing equations are generated. 

**What I did appreciate**  
The main concepts are clearly explained. The balance between equations and text is fine. Most of the equations are "interpreted", and their consequences highlighted. 



Some conventions can be confusing : for example damping matrix is called `L`, and yaw rate is called `r`, longitudinal velocity is called `u`, while `v` is the lateral velocity ... SAE sign conventions are used 
