# CLB -CommandLine Baseball
Access to MLB game informations on terminal.
- author: [prs-watch](http://twitter.com/prs_watch)

[![asciicast](https://asciinema.org/a/MwibFQ1wzeOaNXwyLXwcQwmCe.png)](https://asciinema.org/a/MwibFQ1wzeOaNXwyLXwcQwmCe)

## Agenda
- [Getting Started](#getting-started)
- [Features](#features)
- [Requirement](#requirement)
- [Installation](#installation)
- [Usage](#usage)
- [Options](#options)

## Getting Started
```bash
$ clb -d 20170815
NO              VENUE                  AWAY_TEAM          HOME_TEAM       RESULT
================================================================================
0            Chase Field             Astros(73-46)      D-backs(66-53)     9-4  
1           Nationals Park           Angels(61-59)     Nationals(71-46)    1-3  
2           Yankee Stadium            Mets(53-64)       Yankees(63-55)     4-5  
3           Rogers Centre             Rays(60-61)      Blue Jays(57-62)    6-4  
4            Marlins Park            Giants(48-73)      Marlins(57-61)     9-4  
5            Fenway Park            Cardinals(61-58)    Red Sox(68-51)     4-10
6            Miller Park             Pirates(58-61)     Brewers(62-59)     1-3  
7           Wrigley Field             Reds(50-70)        Cubs(62-56)       2-1  
8    Globe Life Park in Arlington    Tigers(53-66)      Rangers(58-60)     4-10
9            Target Field            Indians(65-52)      Twins(59-58)      8-1  
10           Coors Field             Braves(53-64)      Rockies(66-53)     4-3  
11         Oakland Coliseum          Royals(60-59)     Athletics(53-67)    8-10
12           Safeco Field            Orioles(59-61)    Mariners(60-61)     1-3  
13          Dodger Stadium          White Sox(45-71)    Dodgers(84-34)     1-6  
14            Petco Park            Phillies(43-74)     Padres(53-66)      4-8

$ clb -d 20170815 -r 0
***	away	***
+----------------+-------------------+-----+
|      TEAM      |       NAME        | POS |
+================+===================+=====+
| Houston Astros |  Carlos Beltran   |  D  |
+----------------+-------------------+-----+
| Houston Astros | Francisco Liriano |  P  |
+----------------+-------------------+-----+
| Houston Astros |  Charlie Morton   |  P  |
+----------------+-------------------+-----+
| Houston Astros |  Tyler Clippard   |  P  |
+----------------+-------------------+-----+
| Houston Astros |   Yuli Gurriel    | 1B  |
+----------------+-------------------+-----+
| Houston Astros |   Josh Reddick    | RF  |
+----------------+-------------------+-----+
| Houston Astros |  Luke Gregerson   |  P  |
+----------------+-------------------+-----+
| Houston Astros |   Brad Peacock    |  P  |
+----------------+-------------------+-----+
| Houston Astros |  Marwin Gonzalez  | 1B  |
+----------------+-------------------+-----+
| Houston Astros |    Jose Altuve    | 2B  |
+----------------+-------------------+-----+
| Houston Astros |   Juan Centeno    |  C  |
+----------------+-------------------+-----+
| Houston Astros |   Collin McHugh   |  P  |
+----------------+-------------------+-----+
| Houston Astros |  George Springer  | RF  |
+----------------+-------------------+-----+
| Houston Astros |  Jake Marisnick   | CF  |
+----------------+-------------------+-----+
| Houston Astros |    Max Stassi     |  C  |
+----------------+-------------------+-----+
| Houston Astros |    Mike Fiers     |  P  |
+----------------+-------------------+-----+
| Houston Astros |     Ken Giles     |  P  |
+----------------+-------------------+-----+
| Houston Astros |  Dallas Keuchel   |  P  |
+----------------+-------------------+-----+
| Houston Astros |  Jandel Gustave   |  P  |
+----------------+-------------------+-----+
| Houston Astros |    J.D. Davis     | 3B  |
+----------------+-------------------+-----+
| Houston Astros |   Derek Fisher    | RF  |
+----------------+-------------------+-----+
| Houston Astros |   Joe Musgrove    |  P  |
+----------------+-------------------+-----+
| Houston Astros |  Chris Devenski   |  P  |
+----------------+-------------------+-----+
| Houston Astros |   Alex Bregman    | 3B  |
+----------------+-------------------+-----+
| Houston Astros |    James Hoyt     |  P  |
+----------------+-------------------+-----+
| Houston Astros |  Francis Martes   |  P  |
+----------------+-------------------+-----+

***	home	***
+----------------------+------------------+-----+
|         TEAM         |       NAME       | POS |
+======================+==================+=====+
| Arizona Diamondbacks | Jorge De La Rosa |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks | Fernando Rodney  |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |   Jeff Mathis    |  C  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |   Zack Greinke   |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Gregor Blanco   |  O  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Chris Iannetta  |  C  |
+----------------------+------------------+-----+
| Arizona Diamondbacks | David Hernandez  |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |   Adam Rosales   | SS  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  J.D. Martinez   | RF  |
+----------------------+------------------+-----+
| Arizona Diamondbacks | Paul Goldschmidt | 1B  |
+----------------------+------------------+-----+
| Arizona Diamondbacks | Daniel Descalso  | 2B  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  T.J. McFarland  |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Chris Herrmann  |  C  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |   J.J. Hoover    |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Patrick Corbin  |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |    Jake Lamb     | 3B  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Shelby Miller   |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |   Chris Owings   | SS  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |   A.J. Pollock   | CF  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Brandon Drury   | 2B  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Taijuan Walker  |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |    Nick Ahmed    | SS  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Archie Bradley  |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Andrew Chafin   |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |   Ketel Marte    | SS  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Anthony Banda   |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Silvino Bracho  |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Yasmany Tomas   | LF  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |   Zack Godley    |  P  |
+----------------------+------------------+-----+
| Arizona Diamondbacks |  Steve Hathaway  |  P  |
+----------------------+------------------+-----+

$ clb -d 20170815 -b 0
        TEAM           1   2   3   4   5   6   7   8   9   R   H    E
=====================================================================
   Houston Astros      0   5   2   1   0   0   0   0   1   9   13   1
Arizona Diamondbacks   0   0   0   3   1   0   0   0   0   4   8    0
***	Houston Astros	***
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
| BATTING |   NAME    | POS | AB | R | H | RBI | BB | SO | LOB |  AVG  |
+=========+===========+=====+====+===+===+=====+====+====+=====+=======+
|  1-00   | Springer  | RF  | 5  | 1 | 1 |  2  | 0  | 1  |  1  | 0.303 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  2-00   |  Bregman  | SS  | 5  | 1 | 2 |  1  | 0  | 1  |  0  | 0.274 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  3-00   |  Altuve   | 2B  | 4  | 1 | 2 |  0  | 1  | 1  |  1  | 0.364 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  4-00   |  Gurriel  | 1B  | 5  | 0 | 2 |  1  | 0  | 0  |  3  | 0.294 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  5-00   |  Reddick  | LF  | 5  | 0 | 1 |  0  | 0  | 1  |  1  | 0.293 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  6-00   | Davis, J  | 3B  | 3  | 2 | 1 |  0  | 1  | 0  |  2  | 0.188 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  7-00   |  Stassi   |  C  | 4  | 2 | 2 |  2  | 1  | 0  |  3  | 0.500 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  8-00   | Marisnick | CF  | 4  | 2 | 1 |  0  | 1  | 2  |  1  | 0.242 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  9-00   |  Peacock  |  P  | 3  | 0 | 1 |  2  | 0  | 2  |  2  | 0.286 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  9-01   |  Martes   |  P  | 0  | 0 | 0 |  0  | 0  | 0  |  0  |   0   |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  9-02   |  Beltran  | PH  | 1  | 0 | 0 |  0  | 0  | 0  |  1  | 0.243 |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  9-03   | Devenski  |  P  | 0  | 0 | 0 |  0  | 0  | 0  |  0  |   0   |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  9-04   | Gregerson |  P  | 0  | 0 | 0 |  0  | 0  | 0  |  0  |   0   |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
|  9-05   |  Liriano  |  P  | 0  | 0 | 0 |  0  | 0  | 0  |  0  |   0   |
+---------+-----------+-----+----+---+---+-----+----+----+-----+-------+
+-----------+-------+---+---+----+----+----+----+-------+
| PITCHING  |  IP   | H | R | ER | BB | SO | HR |  ERA  |
+===========+=======+===+===+====+====+====+====+=======+
|  Peacock  | 4.200 | 7 | 4 | 4  | 1  | 9  | 0  | 3.300 |
+-----------+-------+---+---+----+----+----+----+-------+
|  Martes   | 1.100 | 0 | 0 | 0  | 0  | 4  | 0  | 4.990 |
+-----------+-------+---+---+----+----+----+----+-------+
| Devenski  |   1   | 1 | 0 | 0  | 1  | 1  | 0  | 2.700 |
+-----------+-------+---+---+----+----+----+----+-------+
| Gregerson |   1   | 0 | 0 | 0  | 0  | 2  | 0  | 3.860 |
+-----------+-------+---+---+----+----+----+----+-------+
|  Liriano  |   1   | 0 | 0 | 0  | 2  | 1  | 0  | 5.840 |
+-----------+-------+---+---+----+----+----+----+-------+

***	Arizona Diamondbacks	***
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
| BATTING |    NAME     | POS | AB | R | H | RBI | BB | SO | LOB |  AVG  |
+=========+=============+=====+====+===+===+=====+====+====+=====+=======+
|  1-00   |  Marte, K   | SS  | 5  | 1 | 2 |  0  | 0  | 2  |  3  | 0.277 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  2-00   |   Pollock   | CF  | 4  | 2 | 1 |  0  | 1  | 0  |  3  | 0.277 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  3-00   |   Lamb, J   | 3B  | 4  | 1 | 1 |  2  | 0  | 2  |  3  | 0.264 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  4-00   | Goldschmidt | 1B  | 4  | 0 | 2 |  1  | 0  | 1  |  0  | 0.320 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  5-00   | Martinez, J | RF  | 4  | 0 | 0 |  0  | 0  | 3  |  3  | 0.283 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  6-00   |  Iannetta   |  C  | 4  | 0 | 1 |  0  | 0  | 3  |  0  | 0.223 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  7-00   |    Drury    | 2B  | 2  | 0 | 0 |  1  | 2  | 1  |  0  | 0.272 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  8-00   |  Herrmann   | LF  | 3  | 0 | 0 |  0  | 0  | 3  |  3  | 0.161 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  8-01   |   Hoover    |  P  | 0  | 0 | 0 |  0  | 0  | 0  |  0  |   0   |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  8-02   |   Rosales   | PH  | 1  | 0 | 0 |  0  | 0  | 0  |  1  | 0.238 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  9-00   |    Banda    |  P  | 1  | 0 | 0 |  0  | 0  | 1  |  0  |   0   |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  9-01   |  Blanco, G  | PH  | 1  | 0 | 0 |  0  | 0  | 1  |  3  | 0.246 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  9-02   |   Bracho    |  P  | 0  | 0 | 0 |  0  | 0  | 0  |  0  |   0   |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
|  9-03   |  Descalso   | LF  | 1  | 0 | 1 |  0  | 1  | 0  |  0  | 0.240 |
+---------+-------------+-----+----+---+---+-----+----+----+-----+-------+
+----------+----+---+---+----+----+----+----+-------+
| PITCHING | IP | H | R | ER | BB | SO | HR |  ERA  |
+==========+====+===+===+====+====+====+====+=======+
|  Banda   | 4  | 9 | 8 | 8  | 3  | 3  | 0  | 7.320 |
+----------+----+---+---+----+----+----+----+-------+
|  Bracho  | 2  | 2 | 0 | 0  | 0  | 3  | 0  | 4.380 |
+----------+----+---+---+----+----+----+----+-------+
|  Hoover  | 3  | 2 | 1 | 1  | 1  | 2  | 1  | 4.650 |
+----------+----+---+---+----+----+----+----+-------+

$ clb -d 20170815 -p 0
+--------+-----------+-------------------------------------------------+-------+
| INNING | BATTER_NO |                   DESCRIPTION                   | SCORE |
+========+===========+=================================================+=======+
|   1    |     1     | George Springer lines out sharply to left       |  0-0  |
|        |           | fielder Chris Herrmann.                         |       |
+--------+-----------+-------------------------------------------------+-------+
|   1    |     2     | Alex Bregman singles on a fly ball to center    |  0-0  |
|        |           | fielder A.  J.   Pollock.                       |       |
+--------+-----------+-------------------------------------------------+-------+
|   1    |     3     | Jose Altuve strikes out swinging.               |  0-0  |
+--------+-----------+-------------------------------------------------+-------+
|   1    |     4     | Yuli Gurriel flies out to center fielder A.  J. |  0-0  |
|        |           | Pollock.                                        |       |
+--------+-----------+-------------------------------------------------+-------+
|   1    |     5     | Ketel Marte grounds out, pitcher Brad Peacock   |  0-0  |
|        |           | to first baseman Yuli Gurriel.                  |       |
+--------+-----------+-------------------------------------------------+-------+
|   1    |     6     | A.  J.   Pollock grounds out, shortstop Alex    |  0-0  |
|        |           | Bregman to first baseman Yuli Gurriel.          |       |
+--------+-----------+-------------------------------------------------+-------+
|   1    |     7     | Jake Lamb called out on strikes.                |  0-0  |
+--------+-----------+-------------------------------------------------+-------+
|   2    |     8     | Josh Reddick strikes out swinging.              |  0-0  |
+--------+-----------+-------------------------------------------------+-------+
|   2    |     9     | J.  D.   Davis doubles (2) on a sharp line      |  0-0  |
|        |           | drive to right fielder J.   Martinez.           |       |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    10     | Max Stassi doubles (1) on a sharp ground ball   |  1-0  |
|        |           | to left fielder Chris Herrmann.   J.  D.        |       |
|        |           | Davis scores.                                   |       |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    11     | Jake Marisnick singles on a fly ball to right   |  1-0  |
|        |           | fielder J.  D.   Martinez.   Max Stassi to 3rd. |       |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    12     | Brad Peacock called out on strikes.             |  1-0  |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    13     | George Springer doubles (23) on a sharp line    |  3-0  |
|        |           | drive to center fielder A.  J.   Pollock.   Max |       |
|        |           | Stassi scores.    Jake Marisnick scores.        |       |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    14     | Alex Bregman triples (5) on a line drive to     |  4-0  |
|        |           | right fielder J.  D.   Martinez.   George       |       |
|        |           | Springer scores.                                |       |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    15     | Jose Altuve singles on a line drive to center   |  5-0  |
|        |           | fielder A.   Pollock.                           |       |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    16     | Yuli Gurriel flies out to center fielder A.  J. |  5-0  |
|        |           | Pollock.                                        |       |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    17     | Paul Goldschmidt strikes out on a foul tip.     |  5-0  |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    18     | J.  D.   Martinez flies out to right fielder    |  5-0  |
|        |           | George Springer.                                |       |
+--------+-----------+-------------------------------------------------+-------+
|   2    |    19     | Chris Iannetta called out on strikes.           |  5-0  |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    20     | Josh Reddick pops out to shortstop Ketel Marte. |  5-0  |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    21     | J.  D.   Davis hit by pitch.                    |  5-0  |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    22     | Max Stassi flies out to right fielder J.  D.    |  5-0  |
|        |           | Martinez.   Davis to 2nd.                       |       |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    23     | Anthony Banda intentionally walks Jake          |  5-0  |
|        |           | Marisnick.                                      |       |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    24     | Brad Peacock doubles (1) on a line drive to     |  7-0  |
|        |           | right fielder J.  D.   Martinez.   Davis        |       |
|        |           | scores.    Jake Marisnick scores.               |       |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    25     | George Springer flies out to left fielder Chris |  7-0  |
|        |           | Herrmann.                                       |       |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    26     | Brandon Drury grounds out, third baseman J.     |  7-0  |
|        |           | Davis to first baseman Yuli Gurriel.            |       |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    27     | Chris Herrmann called out on strikes.           |  7-0  |
+--------+-----------+-------------------------------------------------+-------+
|   3    |    28     | Anthony Banda strikes out swinging.             |  7-0  |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    29     | Alex Bregman grounds out, third baseman Jake    |  7-0  |
|        |           | Lamb to first baseman Paul Goldschmidt.         |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    30     | Jose Altuve walks.                              |  7-0  |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    31     | Yuli Gurriel triples (1) on a sharp line drive  |  8-0  |
|        |           | to center fielder A.  J.   Pollock.   Jose      |       |
|        |           | Altuve scores.                                  |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    32     | Josh Reddick grounds out, second baseman        |  8-0  |
|        |           | Brandon Drury to first baseman Paul             |       |
|        |           | Goldschmidt.                                    |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    33     | J.  D.   Davis walks.                           |  8-0  |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    34     | Max Stassi pops out to second baseman Brandon   |  8-0  |
|        |           | Drury.                                          |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    35     | Ketel Marte singles on a ground ball to first   |  8-0  |
|        |           | baseman Yuli Gurriel.                           |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    36     | A.  J.   Pollock doubles (25) on a line drive   |  8-0  |
|        |           | to left fielder Josh Reddick.   Ketel Marte to  |       |
|        |           | 3rd.                                            |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    37     | Jake Lamb doubles (24) on a line drive to       |  8-2  |
|        |           | center fielder Jake Marisnick.   Ketel Marte    |       |
|        |           | scores.    A.   Pollock scores.                 |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    38     | Paul Goldschmidt singles on a soft ground ball  |  8-2  |
|        |           | to third baseman J.  D.   Davis.                |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    39     | J.  D.   Martinez strikes out swinging.         |  8-2  |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    40     | Chris Iannetta singles on a line drive to       |  8-2  |
|        |           | center fielder Jake Marisnick.   Jake Lamb to   |       |
|        |           | 3rd.    Paul Goldschmidt to 2nd.                |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    41     | Brandon Drury walks.   Jake Lamb scores.        |  8-3  |
|        |           | Paul Goldschmidt to 3rd.    Chris Iannetta to   |       |
|        |           | 2nd.                                            |       |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    42     | Chris Herrmann strikes out swinging.            |  8-3  |
+--------+-----------+-------------------------------------------------+-------+
|   4    |    43     | Gregor Blanco strikes out swinging.             |  8-3  |
+--------+-----------+-------------------------------------------------+-------+
|   5    |    44     | Jake Marisnick called out on strikes.           |  8-3  |
+--------+-----------+-------------------------------------------------+-------+
|   5    |    45     | Brad Peacock called out on strikes.             |  8-3  |
+--------+-----------+-------------------------------------------------+-------+
|   5    |    46     | George Springer strikes out swinging.           |  8-3  |
+--------+-----------+-------------------------------------------------+-------+
|   5    |    47     | Ketel Marte singles on a sharp ground ball to   |  8-3  |
|        |           | left fielder Josh Reddick.                      |       |
+--------+-----------+-------------------------------------------------+-------+
|   5    |    48     | A.  J.   Pollock grounds into a force out,      |  8-3  |
|        |           | third baseman J.  D.   Davis to second baseman  |       |
|        |           | Jose Altuve.   Ketel Marte out at 2nd.    A.    |       |
|        |           | Pollock to 1st.                                 |       |
+--------+-----------+-------------------------------------------------+-------+
|   5    |    49     | Jake Lamb called out on strikes.                |  8-3  |
+--------+-----------+-------------------------------------------------+-------+
|   5    |    50     | Paul Goldschmidt doubles (27) on a sharp ground |  8-4  |
|        |           | ball to left fielder Josh Reddick.   A.         |       |
|        |           | Pollock scores.  Paul Goldschmidt advances to   |       |
|        |           | 3rd, on a throwing error by shortstop Alex      |       |
|        |           | Bregman.                                        |       |
+--------+-----------+-------------------------------------------------+-------+
|   5    |    51     | J.  D.   Martinez strikes out swinging.         |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   6    |    52     | Alex Bregman pops out to third baseman Jake     |  8-4  |
|        |           | Lamb.                                           |       |
+--------+-----------+-------------------------------------------------+-------+
|   6    |    53     | Jose Altuve grounds out softly, pitcher Silvino |  8-4  |
|        |           | Bracho to first baseman Paul Goldschmidt.       |       |
+--------+-----------+-------------------------------------------------+-------+
|   6    |    54     | Yuli Gurriel singles on a sharp ground ball to  |  8-4  |
|        |           | right fielder J.  D.   Martinez.                |       |
+--------+-----------+-------------------------------------------------+-------+
|   6    |    55     | Josh Reddick singles on a ground ball to center |  8-4  |
|        |           | fielder A.   Pollock.   Yuli Gurriel to 2nd.    |       |
+--------+-----------+-------------------------------------------------+-------+
|   6    |    56     | J.  D.   Davis grounds into a force out,        |  8-4  |
|        |           | fielded by third baseman Jake Lamb.   Yuli      |       |
|        |           | Gurriel out at 3rd.                             |       |
+--------+-----------+-------------------------------------------------+-------+
|   6    |    57     | Chris Iannetta strikes out swinging.            |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   6    |    58     | Brandon Drury called out on strikes.            |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   6    |    59     | Chris Herrmann called out on strikes.           |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   7    |    60     | Max Stassi walks.                               |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   7    |    61     | Jake Marisnick strikes out swinging.            |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   7    |    62     | Carlos Beltran grounds into a double play,      |  8-4  |
|        |           | second baseman Brandon Drury to shortstop Ketel |       |
|        |           | Marte to first baseman Paul Goldschmidt.   Max  |       |
|        |           | Stassi out at 2nd.                              |       |
+--------+-----------+-------------------------------------------------+-------+
|   7    |    63     | Daniel Descalso singles on a line drive to      |  8-4  |
|        |           | right fielder George Springer.                  |       |
+--------+-----------+-------------------------------------------------+-------+
|   7    |    64     | Ketel Marte strikes out swinging.               |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   7    |    65     | A.  J.   Pollock walks.   Daniel Descalso to    |  8-4  |
|        |           | 2nd.                                            |       |
+--------+-----------+-------------------------------------------------+-------+
|   7    |    66     | Jake Lamb grounds into a double play, first     |  8-4  |
|        |           | baseman Yuli Gurriel to shortstop Alex Bregman  |       |
|        |           | to pitcher Chris Devenski.   Pollock out at     |       |
|        |           | 2nd.                                            |       |
+--------+-----------+-------------------------------------------------+-------+
|   8    |    67     | George Springer grounds out, shortstop Ketel    |  8-4  |
|        |           | Marte to first baseman Paul Goldschmidt.        |       |
+--------+-----------+-------------------------------------------------+-------+
|   8    |    68     | Alex Bregman strikes out swinging.              |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   8    |    69     | Jose Altuve doubles (35) on a sharp line drive  |  8-4  |
|        |           | to left fielder Daniel Descalso.                |       |
+--------+-----------+-------------------------------------------------+-------+
|   8    |    70     | Yuli Gurriel flies out to right fielder J.  D.  |  8-4  |
|        |           | Martinez.                                       |       |
+--------+-----------+-------------------------------------------------+-------+
|   8    |    71     | Paul Goldschmidt grounds out, third baseman J.  |  8-4  |
|        |           | D.   Davis to first baseman Yuli Gurriel.       |       |
+--------+-----------+-------------------------------------------------+-------+
|   8    |    72     | J.  D.   Martinez strikes out swinging.         |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   8    |    73     | Chris Iannetta strikes out swinging.            |  8-4  |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    74     | Josh Reddick pops out to third baseman Jake     |  8-4  |
|        |           | Lamb.                                           |       |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    75     | J.  D.   Davis grounds out, third baseman Jake  |  8-4  |
|        |           | Lamb to first baseman Paul Goldschmidt.         |       |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    76     | Max Stassi homers (1) on a fly ball to center   |  9-4  |
|        |           | field.                                          |       |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    77     | Jake Marisnick flies out to right fielder J.    |  9-4  |
|        |           | D.   Martinez.                                  |       |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    78     | Brandon Drury walks.                            |  9-4  |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    79     | Adam Rosales lines out sharply to shortstop     |  9-4  |
|        |           | Alex Bregman.                                   |       |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    80     | Daniel Descalso walks.   Brandon Drury to 2nd.  |  9-4  |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    81     | Ketel Marte strikes out swinging.               |  9-4  |
+--------+-----------+-------------------------------------------------+-------+
|   9    |    82     | A.  J.   Pollock grounds into a force out,      |  9-4  |
|        |           | shortstop Alex Bregman to second baseman Jose   |       |
|        |           | Altuve.   Daniel Descalso out at 2nd.           |       |
+--------+-----------+-------------------------------------------------+-------+

$ clb -d 20170815 -p 0 -s
+--------+-------------------------------------------------------------+-------+
| INNING |                         DESCRIPTION                         | SCORE |
+========+=============================================================+=======+
|   2    | Max Stassi doubles (1) on a sharp ground ball to left       |  1-0  |
|        | fielder Chris Herrmann.   J.  D.   Davis scores.            |       |
+--------+-------------------------------------------------------------+-------+
|   2    | George Springer doubles (23) on a sharp line drive to       |  3-0  |
|        | center fielder A.  J.   Pollock.   Max Stassi scores.       |       |
|        | Jake Marisnick scores.                                      |       |
+--------+-------------------------------------------------------------+-------+
|   2    | Alex Bregman triples (5) on a line drive to right fielder   |  4-0  |
|        | J.  D.   Martinez.   George Springer scores.                |       |
+--------+-------------------------------------------------------------+-------+
|   3    | Brad Peacock doubles (1) on a line drive to right fielder   |  7-0  |
|        | J.  D.   Martinez.   Davis scores.    Jake Marisnick        |       |
|        | scores.                                                     |       |
+--------+-------------------------------------------------------------+-------+
|   4    | Yuli Gurriel triples (1) on a sharp line drive to center    |  8-0  |
|        | fielder A.  J.   Pollock.   Jose Altuve scores.             |       |
+--------+-------------------------------------------------------------+-------+
|   4    | Jake Lamb doubles (24) on a line drive to center fielder    |  8-2  |
|        | Jake Marisnick.   Ketel Marte scores.    A.   Pollock       |       |
|        | scores.                                                     |       |
+--------+-------------------------------------------------------------+-------+
|   4    | Brandon Drury walks.   Jake Lamb scores.    Paul            |  8-3  |
|        | Goldschmidt to 3rd.    Chris Iannetta to 2nd.               |       |
+--------+-------------------------------------------------------------+-------+
|   5    | Paul Goldschmidt doubles (27) on a sharp ground ball to     |  8-4  |
|        | left fielder Josh Reddick.   A.   Pollock scores.  Paul     |       |
|        | Goldschmidt advances to 3rd, on a throwing error by         |       |
|        | shortstop Alex Bregman.                                     |       |
+--------+-------------------------------------------------------------+-------+
|   9    | Max Stassi homers (1) on a fly ball to center field.        |  9-4  |
+--------+-------------------------------------------------------------+-------+
```

## Features
- Access to MLB game informations on terminal.
- Quick way to check MLB game informations.
- Easy tool to use.

## Requirement
To install CLB, you have to install Python 3.5.2+.  
(Sorry, I don't know whether this works well under version < 3.5.2)

## Installation
```
$ pip install commandline-baseball
```

## Usage
#### Check all games on specific date
```bash
$ clb -d ${date you want to check}
```

#### Check boxscore on specific game
```bash
$ clb -d ${date you want to check} -b ${game_no}
```

#### Check play-by-play on specific game
```bash
$ clb -d ${date you want to check} -p ${game_no}
```

#### Check scoring-play on specific game
```bash
$ clb -d ${date you want to check} -p ${game_no} -s
```

#### Check roster on specific game
```bash
$ clb -d ${date you want to check} -r ${game_no}
```

## Options
| OPTION | NOTE                                                                |
| :--:   | :--                                                                 |
| -d     | Date you want to check. (YYYYMMDD)                                  |
| -b     | Game No you want to check boxscore.                                 |
| -p     | Game No you want to check play-by-play.                             |
| -s     | If you want to check scoring play only, add this option after `-p`. |
| -r     | Game No you want to check roster.                                   |
