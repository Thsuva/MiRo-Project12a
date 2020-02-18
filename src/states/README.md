# MiRo-Project12a - states

This folder contains the files that are needed for the state machine architecture.

By Jacopo Favaro, Fabrizio Zavanone.

## The modules

* **src/states/idle.py**: the first state of the state machine waits for the "wake up word" and goes to active state when hears it.
* **src/states/active.py**: this state listens from the `/speech_to_text` topic and tries to get enough information to start the "look for object" routine.
* **src/states/dummy_lfo.py**: dummy state which will contain functions to move the robot and locate the desired object.
* **src/states/dummy_mto.py**: dummy state which will move the robot towards his destination.
* **src/states/failure.py**: state of passage where MiRo signals the failure of one of his actions before getting back to idle state: MiRo puts down his head and moves his ears in a sad behaviour.
* **src/states/happy.py**: final state in which MiRo signals the completion of his objective before shutting down: MiRo moves his tail and reacts to external stimuli like the touch of his head and body.
