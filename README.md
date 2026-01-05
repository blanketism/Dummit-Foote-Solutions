# Solutions to Dummit Foote

An unofficial solutions manual for *Abstract Algebra, 3rd Edition*, by David S. and Richard M. Foote.

Please submit a pull request on your own fork of this repository if you have any changes you'd like to be implemented, and I will get to them as soon as I can to merge later on.

Much of the important messages necessary to be said are in the Preface of `dummit_foote_exercises.pdf`, but again, this is an ongoing project and I am no way affiliated with the authors.

## Downloads

- `dummit_foote_exercises.tex` is the main file that houses `\begin{document}...` and other files that are necessary to compile the entire document.
- `exercises/` is the directory that houses all the exercises, seperated by chapter.
- `commands.tex` and `environments.tex` in the `Base Tex Files/` directory are my own creations for custom commands and environments. Much of the environments are not used in the solutions manual, but may prove useful to readers that are not using more sophisticated environment packages, such as `mdframed` or `tcolorbox`.
- `Misc Environments/` is a directory that houses the `\begin{breakablealgorithm}...` environment used twice in Chapter 0 of the solutions manual, where the authors request the student to code two algorithms regarding GCD and modular arithmetic. Please see the StackExchange thread [here](https://tex.stackexchange.com/questions/33866/algorithm-tag-and-page-break).
