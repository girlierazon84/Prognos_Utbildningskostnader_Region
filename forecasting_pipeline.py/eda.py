"""Module 3: Exploratory Data Analysis"""


import sqlite3
import pandas as pd
import plotly.express as px
from data_loading import (
    DB_PATH,
    load_data,
)

DATABASE_PATH = DB_PATH
tables = load_data(DATABASE_PATH)

def visualize_birth_data(birth_data):
    """Visualize birth trends over the years."""
    fig_birth = px.line(
        birth_data,
        x='Year',
        y='Birthrate',
        color='Region',
        title="Birthrate Trends by Region",
        labels={'Birthrate': 'No. of Births', 'Year': 'Year'},
        hover_data={'Region': True, 'Year': True, 'Birthrate': True}
    )
    fig_birth.show()

def visualize_mortality_data(mortality_data):
    """Visualize mortality rates by age."""
    fig_mortality = px.box(
        mortality_data,
        x='Year',
        y='Deathrate',
        color='Region',
        title="Mortality Rates by Region & Age",
        labels={
            'Deathrate': 'No. of Deaths',
            'Year': 'Year'
            },
        hover_data={
            'Region': True,
            'Year': True,
            'Age': True,
            'Deathrate': True
            }
    )
    fig_mortality.show()

def visualize_migration_data(migration_data):
    """Visualize migration rates by region."""
    fig_migration = px.scatter(
        migration_data,
        x='Year',
        y='Migrationrate',
        color='Region',
        title="Migration Rates by Region & Age",
        labels={
            'Migrationrate': 'No. of Children Migrants',
            'Year': 'Year'
            },
        hover_data={
            'Region': True,
            'Year': True,
            'Age': True,
            'Migrationrate': True
            }
    )
    fig_migration.show()

def visualize_population_data(population_data):
    """Visualize Population (0-19 years old) by Region & Age."""
    fig_migration = px.scatter(
        population_data,
        x='Year',
        y='Population',
        color='Region',
        title="Population (0-19 years old) by Region & Age",
        labels={
            'Population': 'Total Population of Children Ages 0-19',
            'Year': 'Year'
            },
        hover_data={
            'Region': True,
            'Year': True,
            'Age': True,
            'Population': True
            }
    )
    fig_migration.show()

def visualize_costs_data(grundskola_costs, gymnasieskola_costs):
    """Visualize costs per child over the years."""
    fig_costs = px.line(
        grundskola_costs,
        x='Year',
        y='Current Costs',
        title="Grundskola Costs per Child Over the Years",
        labels={'Current Costs': 'Cost per Child (kr)', 'Year': 'Year'},
        hover_data={'Year': True, 'Current Costs': True}
    )
    fig_costs.add_scatter(
        x=gymnasieskola_costs['Year'],
        y=gymnasieskola_costs['Current Cost'],
        mode='lines',
        name='Gymnasieskola Costs per Child'
    )
    fig_costs.show()
