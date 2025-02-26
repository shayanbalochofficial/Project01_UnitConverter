import streamlit as st

# Define units and conversion factors (to base unit)
# Length (base: meter)
length_units = ['cm', 'm', 'km', 'in', 'ft', 'yd', 'mi']
length_factors = {
    'cm': 0.01,        # 1 cm = 0.01 m
    'm': 1.0,          # base unit
    'km': 1000.0,      # 1 km = 1000 m
    'in': 0.0254,      # 1 inch = 0.0254 m
    'ft': 0.3048,      # 1 foot = 0.3048 m
    'yd': 0.9144,      # 1 yard = 0.9144 m
    'mi': 1609.34      # 1 mile = 1609.34 m
}

# Mass (base: kilogram)
mass_units = ['g', 'kg', 't', 'mg', 'lb', 'oz', 'µg']
mass_factors = {
    'g': 0.001,        # 1 g = 0.001 kg
    'kg': 1.0,         # base unit
    't': 1000.0,       # 1 tonne = 1000 kg
    'mg': 1e-6,        # 1 mg = 10^-6 kg
    'lb': 0.453592,    # 1 pound = 0.453592 kg
    'oz': 0.0283495,   # 1 ounce = 0.0283495 kg
    'µg': 1e-9         # 1 microgram = 10^-9 kg
}

# Time (base: second)
time_units = ['s', 'min', 'h', 'day', 'week', 'month', 'year']
time_factors = {
    's': 1.0,          # base unit
    'min': 60.0,       # 1 min = 60 s
    'h': 3600.0,       # 1 hour = 3600 s
    'day': 86400.0,    # 1 day = 86400 s
    'week': 604800.0,  # 1 week = 604800 s
    'month': 2.628e6,  # ~30.44 days
    'year': 3.154e7    # ~365.25 days
}

# Speed (base: m/s)
speed_units = ['m/s', 'km/h', 'mph']
speed_factors = {
    'm/s': 1.0,        # base unit
    'km/h': 0.277778,  # 1000 m / 3600 s
    'mph': 0.44704     # 1609.34 m / 3600 s
}

# Energy (base: joule)
energy_units = ['J', 'kJ', 'kcal']
energy_factors = {
    'J': 1.0,          # base unit
    'kJ': 1000.0,      # 1 kJ = 1000 J
    'kcal': 4184.0     # 1 kcal = 4184 J
}

# Pressure (base: pascal)
pressure_units = ['Pa', 'bar', 'atm']
pressure_factors = {
    'Pa': 1.0,         # base unit
    'bar': 100000.0,   # 1 bar = 100000 Pa
    'atm': 101325.0    # 1 atm = 101325 Pa
}

# Temperature units (handled separately)
temperature_units = ['°C', '°F', 'K']

# Generic conversion function for multiplicative types
def convert_multiplicative(value: float, from_unit: str, to_unit: str, factors: dict[str, float]) -> float:
    value_in_base = value * factors[from_unit]
    result = value_in_base / factors[to_unit]
    return result

# Temperature conversion function
def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    if from_unit == to_unit:
        return value
    elif from_unit == '°C' and to_unit == '°F':
        return (value * 9/5) + 32
    elif from_unit == '°F' and to_unit == '°C':
        return (value - 32) * 5/9
    elif from_unit == '°C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'K' and to_unit == '°C':
        return value - 273.15
    elif from_unit == '°F' and to_unit == 'K':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K' and to_unit == '°F':
        return (value - 273.15) * 9/5 + 32
    return value  # Default case if no conversion applies

# Streamlit app setup
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="wide")
st.markdown("""
    <style>
    .header { text-align: center; }
    .footer { text-align: center; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="header"><h1>📏 Unit Converter</h1><p>🔄 Convert units effortlessly!</p></div>', unsafe_allow_html=True)

# Conversion type selection
type_options = ["Length", "Mass", "Temperature", "Time", "Speed", "Energy", "Pressure"]
selected_type = st.selectbox("Select conversion type", type_options)

# Assign units and factors based on type
if selected_type == "Length":
    units = length_units
    factors = length_factors
elif selected_type == "Mass":
    units = mass_units
    factors = mass_factors
elif selected_type == "Time":
    units = time_units
    factors = time_factors
elif selected_type == "Speed":
    units = speed_units
    factors = speed_factors
elif selected_type == "Energy":
    units = energy_units
    factors = energy_factors
elif selected_type == "Pressure":
    units = pressure_units
    factors = pressure_factors
else:  # Temperature
    units = temperature_units
    factors = None  # No factors needed for temperature

# Unit selection and value input
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("Convert from", units)
with col2:
    to_unit = st.selectbox("Convert to", units)
value = st.number_input("Enter value", value=1.0, step=0.1)

# Perform conversion
if st.button("Convert"):
    if selected_type != "Temperature":
        result = convert_multiplicative(value, from_unit, to_unit, factors)
    else:
        result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.markdown('<div class="footer">🚀 Made by Shayan Baloch</div>', unsafe_allow_html=True)