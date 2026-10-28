# ASCII fallback for exercise boxes

Exercise source files are UTF-8. If the editor or terminal cannot draw `┌`, `┐`, `│`, `─`, `☐`, or `✓`, the text remains ordinary Python comments and all instruction wording is still readable. In VS Code, reopen the file as UTF-8 first.

The same sections can be read with this plain ASCII outline:

~~~text
+-- EXERCISE ----------------------------------------------+
| ID, title, level, difficulty, type, prerequisites        |
+-- OBJECTIVE ---------------------------------------------+
| what to learn and why                                     |
+-- SCENARIO ----------------------------------------------+
| who uses this and what problem they solve                 |
+-- TASKS --------------------------------------------------+
| [ ] implement the specified behavior                      |
| [ ] check the sample and boundary cases                   |
+-- INPUT / OUTPUT / SYNTAX / TODO / VERIFY / HELP --------+
| inspect the labeled source comments and keep their order  |
+-----------------------------------------------------------+
~~~

`[ ]` means unfinished and `[x]` means completed. The marker is for the learner's own checklist; Python does not update it automatically. Text-answer exercises keep their `.txt` submission plain and use a companion file in `instructions/`.
