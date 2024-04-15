from datetime import timedelta
from datetime import datetime, date
from flask import redirect, render_template, request, session, url_for, flash#, request, session, url_for, redirect
from flask import render_template
import requests
from app import app
from app.forms import LoginForm, SignUpForm


# app.permanent_session_lifetime = timedelta(minutes=15) 
# ...
# this code sets the duration of session data for 15 minutes, 
# which otherwise is by default 30 days.
# ...
@app.route('/')
def hello():
   return render_template('home.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    #loginForm = LoginForm()
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        return f'{email} {password}'
    return render_template('login.html', form=form)

@app.route('/signup', methods = ['GET','POST'])
def signup():
    #signUpForm = signUpForm()
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data 
        return f'{username} {email} {password}'
    return render_template('signup.html', form=form)



def pokemon_info(my_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{my_pokemon}'

    response = requests.get(url)

    if response.ok:
        data = response.json()
        poke_dict = {
        'name' :  data['name'],
        'id' : data['id'], 
        'ability' : data['abilities'][0]['ability']['name'],
        'sprite': data['sprites']['front_default'],
        'catch_time': datetime.now()
        }
    # print(poke_dict)
    return poke_dict

pokemon_catchlist = [] # This list will store all the caught pokemons

pokemon_team = []

@app.route('/pokemon', methods = ['GET','POST'])
def pokemon():
    if request.method == 'POST':
        if 'search-btn' in request.form:
            pokemon_name_id = request.form.get('pokemon_name_id')
            session['pokemon_name_id'] = pokemon_name_id
            #print(pokemon_info(pokemon_name_id))
            #return pokemon_info(pokemon_name_id) #f'Searched for {pokemon_name_id}'
            pokemon_deets = pokemon_info(pokemon_name_id)
            
            if pokemon_deets:
                return render_template('pokemon.html', pokemon_deets=pokemon_deets)
            else: 
                return render_template('pokemon.html')
            
            return render_template('pokemon.html')
        if 'catch-btn' in request.form:
            pokemon_catch_id = session.get('pokemon_name_id')
            #if 'pokemon_catchlist' not in session:
            #pokemon_catchlist = session.get('pokemon_catchlist',[])
            if len(pokemon_catchlist)<6:
                if pokemon_catch_id not in pokemon_catchlist:
                    pokemon_catchlist.append(pokemon_catch_id)
                    flash(f' Pokemon {pokemon_catch_id} Caught !')
                elif(len(pokemon_catchlist)==6):
                    print("Pokemon Catch Limit Already Reached! Try releasing the ones you do not want anymore")
                   
                    #flash("Pokemon Catch Limit Already Reached! Try releasing the ones you do not want anymore")

            session['pokemon_catchlist'] = pokemon_catchlist
            pokemon_team = pokemon_catchlist
             
            if pokemon_catchlist : 
                return render_template('pokemon.html', pokemon_catchlist=pokemon_catchlist)
         
    else:
        return render_template('pokemon.html')
@app.route('/team')
def poketeam():
    return render_template('pokemonteam.html')

@app.route('/pokemonteam')
def pokemonteam():
    pokemon_deets =[]
    if 'pokemon_catchlist' in session:
        for pokemon in session['pokemon_catchlist']:
            pokemon_in = pokemon_info(pokemon)
            pokemon_deets.append(pokemon_in)
           # pokemon_deets = pokemon_info(pokemon)
        return render_template('pokemonteam.html', pokemon_deets=pokemon_deets, pokemon_catchlist=pokemon_catchlist)

@app.route('/release/<pokemon_name_id>')
def release_pokemon():
    if request.method == 'POST':
        if 'release-btn' in request.form: 
            pokemon_catchlist.remove(pokemon)
        return render_template('pokemonteam.html', pokemon_catchlist=pokemon_catchlist)
    else: 
        return render_template('pokemonteam.html')