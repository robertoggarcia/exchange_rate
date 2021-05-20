# Exchange rate service
Web service which exposes the current exchange rate of USD to MXN from three
different sources in the same endpoint. Exchange rate sources:
* [Diario Oficial de la Federación](https://www.banxico.org.mx/tipcamb/tipCamMIAction.do) - No API provided, so you will need to scrape the site
* [Fixer](https://fixer.io/) - Well documented API in JSON format
* [Banxico](https://www.banxico.org.mx/SieAPIRest/service/v1/doc/consultaDatosSerieRango) - Service SF43718. API returns XML.

### Running server

* Run server `python manage.py runserver`

### Running unit tests

* Run unit tests `python manage.py tests`

### Cron jobs
In order to execute the command to request the lastest exchage rate for each
 service provider use the following command. Consider use a linux cron or
  kind of service [Cronicle](http://cronicle.net/):
- __Diario Oficial de la Federación__ service provider request: `python manage.py diario_oficial_provider`
- __Fixer__ service provider request: `python manage.py fixer_provider`
- __Banxico__ service provider request: `python manage.py banxico_provider`

### .env

* Django __secret key__: `DJANGO_SECRET_KEY=h+fwx4a2+3(!64jcprhlom=+!1uyqn
*@agi93+5xf4a+b%p4+$`
* User __rate limit__ configuration: `RATE_LIMIT=1000/day`
* Fixer __API KEY__ for request: `FIXER_API_KEY=api_key`
* Fixer __URL__ service: `FIXER_URL=http://data.fixer.io/api/`
* __Currency base__ for exchange rate (for free account use EUR): `FIXER_BASE
=USD`
* Banxico request __TOKEN__: `BANXICO_TOKEN=token`
* Banxico service __URL__: `BANXICO_URL=https://www.banxico.org.mx/SieAPIRest/service/v1/series/`
* MXN Banxico Serie ID: `BANXICO_SERIE=SF43718`
* __Diario Oficial de la Federación__ service URL: `DIARIO_OFICIAL_URL=https://www.banxico.org.mx/tipcamb/tipCamMIAction.do`
* Table exchange rate HTML position: `DIARIO_OFICIAL_TABLE_POSITION=6`
* Interest row position: `DIARIO_OFICIAL_ROW_POSITION=2`
* Interest column position with exchange rate: `DIARIO_OFICIAL_COLUMN=3`

# The High Level Problem
You are the tech lead for a new Credijusto project that collects client information to be run
through risk models to determine if they are viable candidates for our loan products. The
project has integrations to 3rd party systems like Buró de Crédito, where we can obtain
pertinent client financial information to help Credijusto assess the client risk profile. In order
to launch this project, we need a production test plan. Please outline, in as much detail as
you can the types of tests you would run, how you would run these tests in a live production
environment, and how you accomplish running these tests given you have live 3rd party
integrations.

__R__: In this scenario we would use a hybrid approach that includes live
 testing and mock testing. Live tests would be making requests directly to 
3PA, ideally you would configure an account or credentials that allow us 
to identify those test requests to eventually analyze them. For mock tests, 
we would use a proxy that emulates the contracts defined for the responses of 
this 3PA, so that we simulate its good behavior and specifically test our
 system. 

An important point to determine is the priority of each of these tests, that is; 
If most of the problems come from 3PA we would have to give priority to the 
execution of live tests, considering that the execution time of this type of 
tests is longer given the http requests that have to wait, in addition to the 
fact that the 3PA could present false positives due to application load or
 fails. 

On the other hand, if our system is the one with the highest number of 
failures, we would give priority to mock tests, to ensure the integrity of 
our project against the expected responses of 3PA. I believe that both tests 
are important to be covered against the disadvantages of each one: the delay 
and false positives in live tests and the lack of coverage of the mock against 
the 3PA that we can't control.

# The Scenario Problem
Several services for which your team is responsible depend on another squad’s service in
production, and mocks of that service in development and staging.

Your team uses the mocks they have provided in both development and staging. However,
there are regular incidents in staging and production due to code changes made by that
team which they have not propagated to their mocks.
Your developers are frustrated and losing confidence in their coworkers. The tech lead from
the other squad is an E2 developer and has a reputation for over-confidence and being
difficult to work with.

How do you handle this situation?

__R__: First, I would speak with the tech lead using a model known 
as COIN, where I provide **C**ontext for the problem, mention specific
 **O**bservations, emphasize the **I**mpact on the product and / or project
 , and propose some ideas or **N**xt steps for improvement.

Possible answers:
- It isn't our responsibility: I would emphasize the impact of this problem 
and mention the benefits of collaborating to solve it. In addition, I would 
involve the team in failure alerts or notifications so that they can empathize 
with our problems in a tangible way.

- I don't have time for the call: I would add a couple of alternatives 
to be able to coincide, failing that I would write an email with the details
 of the problem and the possible solutions, trying to find a compromise with 
 the team.

- Those proposals aren't good: Nothing is set in stone, I am open to listening 
to proposals that involve both teams in order to reach a solution.

Once both teach leads understand the impact, talk with the teams and commit
 then with proposals. The important thing is communication, we seek to agree on
how to communicate the changes of this service to our team, it can be a 
format for each merge within the repository using tools such as slack, 
or creating a channel to notify relevant changes by message or email.