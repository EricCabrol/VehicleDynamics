
NB : the categories below only reflect my personal view. There is no such thing as "truth" here (except may be the market share figures, which I do not have). The most important point when choosing a software is to know if it fits your needs and requirements. 

## Champions
* [IPG CarMaker](https://ipg-automotive.com/fr/produits-et-services/simulation-software/carmaker/), which is probably the heavyweight of this competition, used by many OEM and suppliers. But also the most expensive software, as far as I know :)
* [CarSim](https://www.carsim.com/). The company (Mechanical Simulation) was co-founded in 1996 by Thomas Gillespie, author of a [reference book](https://github.com/EricCabrol/VehicleDynamics/blob/master/books.md) about vehicle dynamics. 
* [VI-CarRealTime](https://www.vi-grade.com/en/products/vi-carrealtime/). The company (VI-Grade) was created in 2005 as a spin-off from MSC Software.
* [Dyna4](https://www.vector.com/int/en/products/products-a-z/software/dyna4/). The company (TESIS) was created in 1992 by Cornelius Chucholowski (who was at that time a freelancer for BMW, in charge of real-time capable vehicle models), and acquired in 2019 by VECTOR.
* [MSC Adams/Car](https://www.mscsoftware.com/fr/product/adamscar) which unlike the others is a multibody solver, hence more "generic" but less computationally efficient (*)
* [MSC Adams Real-Time](https://www.mscsoftware.com/fr/product/adams-real-time) for RT applications
 

## Challengers :
* [Modelon Vehicle Dynamics Library](https://www.modelon.com/library/vehicle-dynamics-library), based on Modelica (... but not free :) )
* [Simcenter Amesim](https://www.plm.automation.siemens.com/global/fr/products/simulation-test/vehicle-dynamics.html) with a dedicated Vehicle Dynamics library
* [Simulink Vehicle Dynamics Blockset](https://www.mathworks.com/products/vehicle-dynamics.html) since Mathworks could not leave the field unoccupied :)
* [AVSimulation Callas](https://www.avsimulation.com/callas-vehicle-dynamics-model-runtime/), included in the SCANeR simulation suite.
* [dSpace ASM Vehicle Dynamics](https://www.dspace.com/en/pub/home/products/sw/automotive_simulation_models/produkte_asm/vehicle_dynamics_models.cfm), probably convenient for users of dSpace hardware.
* [ChassisSim](https://www.chassissim.com/), with the excellent youtube channel animated by Danny Nowlan. Recently partnered with [Altair](https://altairengineering.fr/chassissim/)

## See also :
* [SimVehicleLT](https://www.faac.com/realtime-technologies/products/simvehiclelt/) (not well known)
* [MapleCar](https://www.maplesoft.com/webinars/recorded/featured.aspx?id=1288) : looks like a student project at that time

(*) If you want to know more about the difference between multibody solvers and dedicated vehicle dynamics softwares, you can have a look at the sixth slide of my document [Multibody simulation in 10 slides](https://github.com/EricCabrol/Short_stories/blob/master/multibody_simulation_resources_in_10slides.pdf).
To make it simple, most softwares from the above list use a symbolic formulation for a predefined topology of the model (see for example the [14dof model](https://www.mathworks.com/help/vdynblks/ug/passenger-vehicle-dynamics-models.html) of Mathworks' VD BlockSet). If you want to add a body with its own dynamic, you can't ! But these softwares are fast, around 10 times faster than real-time.  
With Adams/Car on the other hand you can do what you want, but it will (except in its real-time "simplified" version) not be real-time compliant. 
