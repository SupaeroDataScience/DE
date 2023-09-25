# PostgeSQL

In this practical session, we cover many examples of database queries with the
popular DBMS PostgreSQL.

Based on the
[TP](https://lms.isae.fr/pluginfile.php/72351/mod_resource/content/1/labSQLFSD312.pdf)
by Christophe Garion, CC BY-NC-SA 2015.

## Setup

Before class, please install PostgreSQL and pgAdmin.

### PostgreSQL installation

For this session, students should install [PostgreSQL](https://www.postgresql.org/download/) (v9 or higher) and [pgAdmin](https://www.pgadmin.org/) (v4). Follow the installation instructions and make sure you have an initial database setup and the `postgresql` service running.

+ [Installation on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart)
+ [Installation on Mac OS](https://postgresapp.com/)
+ [Installation on Arch Linux](https://wiki.archlinux.org/index.php/PostgreSQL)
+ [Installation on Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-database)
+ [Installation on Windows](https://www.postgresqltutorial.com/install-postgresql/) (and add the PostgreSQL binaries to your [path](https://www.pcastuces.com/pratique/astuces/5334.htm))

Additionally, add your login user as a postgresql superuser to enable database creation with your user:

```bash
# bash shell in Linux or OSX
$ sudo su -l postgres
[postgres]$ createuser --interactive
```

### pgAdmin

You can do all exercises directly through the `psql` shell for this class. However, it is useful to have a graphical confirmation of the database configuration. pgAdmin is one of many front-ends for Postgres. Install it by following the instructions on the [pgAdmin](https://www.pgadmin.org/) site.

## Setup - database creation

Once you've installated and configured PostgreSQL, create the first exercise database:

```bash
# bash shell in Linux or OSX or windows powershell
$ createdb db-mexico86
```

you can also do this through an SQL shell:

```sql
# SQL shell
postgres=# CREATE DATABASE "db-mexico86";
```

Confirm with pgAdmin that your database `db-mexico86` was created. If you don't
have any servers, create one by right-clicking. The host address is `127.0.0.1`
and the maintenance database and username should be `postgres`.

In pgAdmin, if you are asked for a password and don't know what your password
is, you can reset the password of the postgres user:

<details><summary>change password</summary>

```sql
postgres=# ALTER USER postgres WITH PASSWORD "newpassword";
```

</details>

## Mexico86 database - simple queries

This database contains data from the 1986 football World Cup. 

You can download the database creation script individually:
```bash
$ wget https://raw.githubusercontent.com/SupaeroDataScience/DE/master/scripts/mexico86/create-tables-std.sql
```

Or git clone the class repository and navigate to the creation and insertion [scripts](https://github.com/SupaeroDataScience/DE/tree/master/scripts).

Once you have the scripts, run the database creation script in the `mexico` folder.

```bash
# bash shell in Linux or OSX, or windows powershell
$ psql -d db-mexico86 -f mexico86/create-tables-std.sql
```

If that doesn't work, you can copy the script into the Query Tool in pgAdmin.

**Exercise 1.1**: Look at the database creation scripts. What are the tables being created? What are their fields? Which fields are keys? Confirm these values in pgAdmin.

<details><summary>Response</summary>

Pays: (<u>nom</u>, groupe)
<br/>
Typematch: (<u>type</u>)
<br/>
Match: (<u>paysl, paysv</u>, butsl, butsv, <u>type</u>, date)

</details>

You should be able to make queries now. You can either use PostgreSQL in interactive mode by running 

```
$ psql -d db-mexico86
```

or write your solutions in an SQL file and run the file:

```
$ echo "SELECT groupe FROM pays;" > a.sql
$ psql -d db-mexico86 -f a.sql
```

You can also use the Query Editor in pgAdmin for a graphical interface.
  
**Exercise 1.2**: Write a query which lists the countries participating in the World Cup.

<details><summary>Response</summary>

```
        nom 
---------------------
Argentine
Italie
Bulgarie
Corée
Mexique
Paraguay
Belgique
Irak
URSS
Hongrie
France
Canada
Brésil
Espagne
Irlande du Nord
Algérie
Danemark
RFA
Uruguay
Écosse
Maroc
Angleterre
Pologne
Portugal
(24 rows)
```

</details>

**Exercise 1.3**: Write a query which lists all matches as a pair of countries per match.

<details><summary>Response</summary>

```
        paysl        |        paysv 
---------------------|---------------------
Bulgarie            | Italie
Argentine           | Corée
Italie              | Argentine
Corée               | Bulgarie
Corée               | Italie
Argentine           | Bulgarie
Belgique            | Mexique
Paraguay            | Irak
Mexique             | Paraguay
Irak                | Belgique
Irak                | Mexique
Paraguay            | Belgique
Canada              | France
URSS                | Hongrie
France              | URSS
Hongrie             | Canada
URSS                | Canada
Hongrie             | France
Espagne             | Brésil
Algérie             | Irlande du Nord
Brésil              | Algérie
Irlande du Nord     | Espagne
Irlande du Nord     | Brésil
Algérie             | Espagne
Uruguay             | RFA
Écosse              | Danemark
Danemark            | Uruguay
RFA                 | Écosse
Écosse              | Uruguay
Danemark            | RFA
Maroc               | Pologne
Portugal            | Angleterre
Angleterre          | Maroc
Pologne             | Portugal
Angleterre          | Pologne
Maroc               | Portugal
Brésil              | Pologne
France              | Italie
Maroc               | RFA
Mexique             | Bulgarie
Argentine           | Uruguay
Angleterre          | Paraguay
URSS                | Belgique
Espagne             | Danemark
Brésil              | France
RFA                 | Mexique
Argentine           | Angleterre
Belgique            | Espagne
France              | RFA
Argentine           | Belgique
RFA                 | Argentine
(51 rows)
```

</details>

**Exercise 1.4**: Write a query which lists the matches which took place on June 5, 1986.

<details><summary>Response</summary>

```
        paysl        |   paysv
---------------------|-----------
Italie              | Argentine
Corée               | Bulgarie
France              | URSS
(3 rows)
```

</details>

**Exercise 1.5**: Write a query which lists the countries which France played against (hint, France could have played either side).

<details><summary>Response</summary>

```
pays
---------
Brésil
Canada
Hongrie
Italie
RFA
URSS
(6 rows)
```

</details>

**Exercise 1.6**: Write a query which returns the winner of the World Cup

<details><summary>Response</summary>

```
pays
-----------
Argentine
(1 row)
```

</details>

## Beer database

We'll now use a database which tracks the beers that a group of friends enjoy. Create the database and populate it using the provided [scripts](https://github.com/SupaeroDataScience/DE/tree/master/scripts).

```bash
$ createdb db-beer
$ psql -d db-beer -f beer/create-tables-std.sql
$ psql -d db-beer -f beer/insert.sql
```

**Exercise 2.1**: Look at the database creation scripts. What are the tables being created? What are their fields? Which fields are keys? Confirm these values in pgAdmin.

<details><summary>Response</summary>

Frequente: (<u>buveur, bar</u>)
<br/>
Sert: (<u>bar, biere</u>)
<br/>
Aime: (<u>buveur, biere</u>)

</details>

Write queries which respond to the following questions. Hint, understanding [natural joins](https://sql.sh/cours/jointures/natural-join) may help.

**Exercise 2.2** What is the list of bars which serve the beer that Martin likes?

<details><summary>Response</summary>

```
        bar 
-------------------
 Ancienne Belgique
 La Tireuse
 Le Filochard
(3 rows)
```

</details>

**Exercise 2.3** What is the list of drinkers who go to at least one bar which servers a beer they like?

<details><summary>Response</summary>

```
 buveur 
--------
 Bob
 David
 Emilie
 Martin
(4 rows)
```

</details>

**Exercise 2.3** What is the list of drinkers who don't go to any bars which serve the beer they like?

<details><summary>Response</summary>

```
 buveur 
--------
 Cecile
 Alice
(2 rows)
```

</details>

## Complex queries - Mexico database

**Exercise 3.1**: Create a table with an entry for each match which lists the **total** number of goals (scored by either side), the match type, and the date. As we'll use this table later on, create a VIEW called "matchbutsglobal" with this information.

<details><summary>Response</summary>

```
        paysl        |        paysv        | buts |  type  |    date 
---------------------+---------------------+------+--------+------------
 URSS                | Belgique            |    7 | 1/8    | 1986-06-15
 France              | Italie              |    2 | 1/8    | 1986-06-17
 Maroc               | Pologne             |    0 | Poule  | 1986-06-02
 RFA                 | Argentine           |    5 | Finale | 1986-06-29
 Brésil              | France              |    2 | 1/4    | 1986-06-21
 Italie              | Argentine           |    2 | Poule  | 1986-06-05
 Maroc               | Portugal            |    4 | Poule  | 1986-06-11
 Brésil              | Algérie             |    1 | Poule  | 1986-06-06
 Paraguay            | Belgique            |    4 | Poule  | 1986-06-11
 Hongrie             | France              |    3 | Poule  | 1986-06-09
 Irak                | Belgique            |    3 | Poule  | 1986-06-08
 Danemark            | RFA                 |    2 | Poule  | 1986-06-13
 Irlande du Nord     | Espagne             |    3 | Poule  | 1986-06-07
 Algérie             | Irlande du Nord     |    2 | Poule  | 1986-06-03
 RFA                 | Mexique             |    0 | 1/4    | 1986-06-21
 URSS                | Hongrie             |    6 | Poule  | 1986-06-02
 Mexique             | Paraguay            |    2 | Poule  | 1986-06-07
 Belgique            | Espagne             |    2 | 1/4    | 1986-06-22
 Irak                | Mexique             |    1 | Poule  | 1986-06-11
 Espagne             | Brésil              |    1 | Poule  | 1986-06-01
 Angleterre          | Maroc               |    0 | Poule  | 1986-06-06
 Irlande du Nord     | Brésil              |    2 | Poule  | 1986-06-12
 Maroc               | RFA                 |    1 | 1/8    | 1986-06-17
 Belgique            | Mexique             |    3 | Poule  | 1986-06-03
 Bulgarie            | Italie              |    2 | Poule  | 1986-05-31
 Écosse              | Uruguay             |    0 | Poule  | 1986-06-13
 Algérie             | Espagne             |    3 | Poule  | 1986-06-12
 Argentine           | Belgique            |    2 | 1/2    | 1986-06-25
 Brésil              | Pologne             |    4 | 1/8    | 1986-06-16
 Danemark            | Uruguay             |    7 | Poule  | 1986-06-08
 Corée               | Italie              |    5 | Poule  | 1986-06-10
 Canada              | France              |    1 | Poule  | 1986-06-01
 Argentine           | Uruguay             |    1 | 1/8    | 1986-06-16
 France              | RFA                 |    2 | 1/2    | 1986-06-25
 France              | URSS                |    2 | Poule  | 1986-06-05
 Uruguay             | RFA                 |    2 | Poule  | 1986-06-04
 Angleterre          | Pologne             |    3 | Poule  | 1986-06-11
 Portugal            | Angleterre          |    1 | Poule  | 1986-06-03
 Écosse              | Danemark            |    1 | Poule  | 1986-06-04
 Angleterre          | Paraguay            |    3 | 1/8    | 1986-06-18
 Hongrie             | Canada              |    2 | Poule  | 1986-06-06
 Argentine           | Corée               |    4 | Poule  | 1986-06-02
 Pologne             | Portugal            |    1 | Poule  | 1986-06-07
 RFA                 | Écosse              |    3 | Poule  | 1986-06-08
 Mexique             | Bulgarie            |    2 | 1/8    | 1986-06-15
 URSS                | Canada              |    2 | Poule  | 1986-06-09
 Espagne             | Danemark            |    6 | 1/8    | 1986-06-18
 Paraguay            | Irak                |    1 | Poule  | 1986-06-04
 Argentine           | Bulgarie            |    2 | Poule  | 1986-06-10
 Argentine           | Angleterre          |    3 | 1/4    | 1986-06-22
 Corée               | Bulgarie            |    2 | Poule  | 1986-06-05
(51 rows)
```

</details>

**Exercise 3.2**: Write a query which caluculates the number of goals scored on average in all the matches of the French team.

<details><summary>Response</summary>

```
    Moyenne buts
--------------------
 2.0000000000000000
(1 row)
```

</details>

**Exercise 3.3**: Write a query which calculates the total number of goals scored *only* by the French team.

<details><summary>Response</summary>

```
 buts 
------
    8
(1 row)
```

</details>

**Exercise 3.4**: Write a query which caluclates the total number of goals scored in each Poule match. Order the results by group.

<details><summary>Response</summary>

```
 groupe | sum 
--------+-----
 A      |  17
 B      |  14
 C      |  16
 D      |  12
 E      |  15
 F      |   9
(6 rows)
```

</details>

**Exercise 3.5**: Write a function `vainquer` which takes in the two countries of a match and the match type and which returns the winner. Apply your function to the following pairs:

```
SELECT * FROM vainqueur('Espagne', 'Danemark', '1/8');
SELECT * FROM vainqueur('Brésil', 'France', '1/4');
```

<details><summary>Response</summary>

```
 vainqueur 
-----------
 Espagne
(1 row)

 vainqueur 
-----------
 Match nul
(1 row)
```

</details>

**Exercise 3.6**: Write a function `butsparequipe` which returns the total and the average number of points scored by a team. Apply your function to the French team. Bonus points for making the result display the name of the team.

```
SELECT * FROM butsparequipe('France');

```

<details><summary>Response</summary>

```
  pays  | total |      moyenne 
--------+-------+--------------------
 France |     8 | 1.3333333333333333
(1 row)
```

</details>

**Exercise 3.7**: Using the `butsparequipe` function, write a query which lists all countries and the points they scored. 

<details><summary>Response</summary>

```
        pays         | total 
---------------------+-------
 Argentine           |    14
 Italie              |     5
 Bulgarie            |     2
 Corée               |     4
 Mexique             |     6
 Paraguay            |     4
 Belgique            |    10
 Irak                |     1
 URSS                |    12
 Hongrie             |     2
 France              |     8
 Canada              |     0
 Brésil              |     9
 Espagne             |    11
 Irlande du Nord     |     2
 Algérie             |     1
 Danemark            |    10
 RFA                 |     8
 Uruguay             |     2
 Écosse              |     1
 Maroc               |     3
 Angleterre          |     7
 Pologne             |     1
 Portugal            |     2
(24 rows)
```

</details>


**Exercise 3.8**: Using the `butsparequipe` function, write a query which shows the country which scored the most points and the number of points they scored.

<details><summary>Response</summary>

```
   pays    | total 
-----------+-------
 Argentine |    14
(1 row)
```

</details>

## Pull the trigger

In this exercise, we're going to create a [TRIGGER](https://sql.sh/cours/create-trigger), a mechanism which allows for automatically executing actions when an event occurs.

Create the `db-trigger` database.

```bash
$ createdb db-trigger
```

**Exercise 4.1**: Create a table `rel(nom, value)` where `nom` is a string of characters and `value` is an integer. `nom` will be the primary key

<details><summary>Solution</summary>

```
CREATE TABLE IF NOT EXISTS rel (
    nom VARCHAR(20),
    valeur INTEGER,
    PRIMARY KEY (nom)
);
```

</details>

**Exercise 4.2**: Add 5 tuples into the table

<details><summary>Solution</summary>

```
INSERT INTO rel VALUES
       ('Alice', 10),
       ('Bob', 5),
       ('Carl', 20),
       ('Denise', 11),
       ('Esther', 6);
```

</details>

**Exercise 4.3**: Write a trigger such that, when adding new tuples, the average value of `val` cannot decrease. If a new tuple is added which would decrease the average, an exception should be raised.

The following insertion should work:

```
INSERT INTO rel VALUES ('Fab', 15);

SELECT * FROM rel;
```

As we can see, the `(Fab, 15)` tuple was added:

```
  nom   | valeur 
--------+--------
 Alice  |     10
 Bob    |      5
 Carl   |     20
 Denise |     11
 Esther |      6
 Fab    |     15
(6 rows)
```


However, the following insertion should give an exception:

```
INSERT INTO rel VALUES ('Guy', 2);
```

<details><summary>Solution</summary>

```
CREATE OR REPLACE FUNCTION verifier_moyenne()
                  RETURNS trigger AS $verifier_moyenne$
    DECLARE
      moyenne FLOAT;
      nb      INTEGER;
    BEGIN
        moyenne := AVG(valeur) FROM rel;
        nb := COUNT(*) FROM rel;

        IF ((nb * moyenne + NEW.valeur) / (nb + 1)) < moyenne THEN
            RAISE EXCEPTION 'problem with insertion: valeur average is decreasing!';
        END IF;

        RETURN NEW;
    END;
$verifier_moyenne$ LANGUAGE plpgsql;

CREATE TRIGGER VerificationMoyenne
BEFORE INSERT ON rel
FOR EACH ROW
EXECUTE PROCEDURE verifier_moyenne();
```

</details>

## Deliverables

For evaluation, you should provide a single PostgreSQL script which reproduces the results of all exercises. You should upload the script to the LMS by October 3.
