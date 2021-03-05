
NB : the categories below only reflect my personal view. There is no such thing as "truth" here (except may be the market share figures, which I do not have). The most important point when choosing a software is to know if it fits your needs and requirements. 

## Champions
* [IPG CarMaker](https://ipg-automotive.com/fr/produits-et-services/simulation-software/carmaker/), which is probably the heavyweight of this competition, used by many OEM and suppliers. But also the most expensive software, as far as I know :)
* [CarSim](https://www.carsim.com/). The company (Mechanical Simulation) was co-founded in 1996 by Thomas Gillespie, author of a [reference book](https://github.com/EricCabrol/VehicleDynamics/blob/master/books.md) about vehicle dynamics. 
* [VI-CarRealTime](https://www.vi-grade.com/en/products/vi-carrealtime/). The company (VI-Grade) was created in 2005 as a spin-off from MSC Software.
* [Dyna4](https://www.vector.com/int/en/products/products-a-z/software/dyna4/). The company (TESIS) was created in 1992 by Cornelius Chucholowski (who was at that time a freelancer for BMW, in charge of real-time capable vehicle models), and acquired in 2019 by VECTOR.
* [MSC Adams/Car](https://www.mscsoftware.com/fr/product/adamscar) which unlike the others is a multibody solver, hence more "generic" but less computationally efficient (*). [Adams Real-Time](https://www.mscsoftware.com/fr/product/adams-real-time) is a "simplified" version for RT applications
 

## Challengers
* [Modelon Vehicle Dynamics Library](https://www.modelon.com/library/vehicle-dynamics-library), based on Modelica (... but not free :) )
* [Simcenter Amesim](https://www.plm.automation.siemens.com/global/fr/products/simulation-test/vehicle-dynamics.html) with a dedicated Vehicle Dynamics library
* [Simulink Vehicle Dynamics Blockset](https://www.mathworks.com/products/vehicle-dynamics.html) 
* [AVSimulation Callas](https://www.avsimulation.com/callas-vehicle-dynamics-model-runtime/), included in the SCANeR simulation suite.
* [dSpace ASM Vehicle Dynamics](https://www.dspace.com/en/pub/home/products/sw/automotive_simulation_models/produkte_asm/vehicle_dynamics_models.cfm)
* [AVL VSM](https://www.avl.com/-/avl-vsm-4-)
* [ChassisSim](https://www.chassissim.com/), with the excellent youtube channel animated by Danny Nowlan. Recently partnered with [Altair](https://altairengineering.fr/chassissim/)
* [RACE Software](https://race.software/)
* [Dynacar](https://www.winemantech.com/products/dynacar-vehicle-simulator/), available as an add-on for NI VeriStand for HIL testing

There are solutions among the majority of simulation software vendors, but knowing how relevant they are would require a full time survey, which I can't afford :)
You can have a look at [SimulationX](https://www.simulationx.com/iti/newsdetail/news/driving-maneuvers-models-for-mbs-vehicle-dynamics-simulation.html) by ESI,  [MapleSoft](https://www.maplesoft.com/solutions/engineering/IndustrySolutions/vehicledynamics.aspx), etc ...

## See also
* [SimVehicle](https://www.faac.com/realtime-technologies/products/simvehiclelt/) (not well known, at least by me)
* [MapleCar](https://www.maplesoft.com/webinars/recorded/featured.aspx?id=1288) : looks like a student project at that time



## On the freeware or open-source side
* [Project Chrono](https://projectchrono.org/) with a a financial support from the US Army
* [MBDyn](https://www.mbdyn.org/) which is a generic multibody solver by a team from Politecnico di Milano
* [OpenVD](https://github.com/andresmendes/openvd) by Andres Mendes, available for Octave (free alternative to Matlab)
* [EoM](https://github.com/BPMinaker/EoM.jl) in Julia, by Bruce Minaker ([his book](https://www.wiley.com/en-bz/Fundamentals+of+Vehicle+Dynamics+and+Modelling:+A+Textbook+for+Engineers+With+Illustrations+and+Examples-p-9781118980095)). Far from a ready to use package, but interesting to understand how the equations are derived
* [MBSymba](http://www.multibody.net/mbsymba/) in the same vein, by Roberto Lot (well known for its academic contributions). But it is Maple based, I think.
* [DynaV](http://brejaud.pascal.pagesperso-orange.fr/index.htm) (last updated in 2006 !) if you can read french, and are still reading this page ... :) 


---

(*) If you want to know more about the difference between multibody solvers and dedicated vehicle dynamics softwares, you can have a look at the sixth slide of my document [Resources for Multibody simulation](https://github.com/EricCabrol/Short_stories/blob/master/multibody_simulation_resources_in_10slides.pdf).
To make it simple, most softwares from the above list use a symbolic formulation for a predefined topology of the model (see for example the [14dof model](https://www.mathworks.com/help/vdynblks/ug/passenger-vehicle-dynamics-models.html) of Mathworks' VD BlockSet).  
If you want to add a body with its own dynamic, you can't ! But these softwares are fast, around 10 times faster than real-time.  

With Adams/Car on the other hand you can do what you want in terms of topology, but it has a strong impact on CPU performance : it depends a lot on the complexity level of the model of course, but with a very rough approximation Adams/Car is 10 times slower than real-time, and Adams-RT is barely fast enough to be used on RT platforms.

There are of course other major differences between the two families (such as hardpoints vs elasto-kinematic maps), but it would go beyond the scope of this page ...
