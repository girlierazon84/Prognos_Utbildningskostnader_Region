"""Module 2: Data Preprocessing"""


from data_loading import load_data


DB_PATH = r'C:\Users\girli\OneDrive\Desktop\Projekt_Data_Science\Final\birthrate_education_costs.db'

tables = load_data(DB_PATH)
table_data = load_data(tables[
    'birth_data',
    'mortality_data',
    'migration_data',
    'population_0_16',
    'population_17_19',
    'grundskola_costs',
    'gymnasieskola_costs'
    ])

def preprocess_birth_data(birth_data):
    """Preprocess and pivot birth data."""
    birth_data['Region'] = birth_data['region_code'].astype(str) + " - " + birth_data['region_name']
    birth_data['Year'] = birth_data['year'].astype(int)
    birth_data['Birthrate'] = birth_data['number'].astype(int)
    return birth_data[['Region', 'Year', 'Birthrate']]

def preprocess_mortality_data(mortality_data):
    """Preprocess mortality data."""
    mortality_data['Region'] = mortality_data['region_code'].astype(str) + " - " + mortality_data['region_name']
    mortality_data['Year'] = mortality_data['year'].astype(int)
    mortality_data['Age'] = mortality_data['age'].astype(int)
    mortality_data['Deathrate'] = mortality_data['number'].astype(int)
    return mortality_data[['Region', 'Year', 'Age', 'Deathrate']]

def preprocess_migration_data(migration_data):
    """Preprocess migration data."""
    migration_data['Region'] = migration_data['region_code'].astype(str) + " - " + migration_data['region_name']
    migration_data['Year'] = migration_data['year'].astype(int)
    migration_data['Age'] = migration_data['age'].astype(int)
    migration_data['Migrationrate'] = migration_data['number'].astype(int)
    return migration_data[['Region', 'Year', 'Age', 'Migrationrate']]

def preprocess_population_data(population_data):
    """Preprocess population data."""
    population_data['Region'] = population_data['region_code'].astype(str) + " - " + population_data['region_name']
    population_data['Year'] = population_data['year'].astype(int)
    population_data['Age'] = population_data['age'].astype(int)
    population_data['Population'] = population_data['population'].astype(int)
    return population_data[['Region', 'Year', 'Age', 'Population']]

def preprocess_grundskola_costs_data(grundskola_costs):
    """Preprocess grundskola costs data."""
    grundskola_costs['Year'] = grundskola_costs['year'].astype(int)
    grundskola_costs['Fixed Costs'] = grundskola_costs['fixed_cost_per_child_kr'].astype(float)
    grundskola_costs['Current Costs'] = grundskola_costs['current_cost_per_child_kr'].astype(float)
    return grundskola_costs[['Year', 'Fixed Costs', 'Current Costs']]

def preprocess_gymnasieskola_costs_data(gymnasieskola_costs):
    """Preprocess gymnasieskola costs data."""
    gymnasieskola_costs['Year'] = gymnasieskola_costs['year'].astype(int)
    gymnasieskola_costs['Fixed Cost'] = gymnasieskola_costs['fixed_cost_per_child_kr'].astype(float)
    gymnasieskola_costs['Current Cost'] = gymnasieskola_costs['current_cost_per_child_kr'].astype(float)
    return gymnasieskola_costs[['Year', 'Fixed Cost', 'Current Cost']]
