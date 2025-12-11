import streamlit

streamlit.title("RETC Savings Calculator")
streamlit.write("Let's calculate your RETC savings!")
streamlit.write("This calculator is accurate as of 12/10/2025")

#default placeholder rate
#rate = streamlit.number_input("Placeholder rate", min_value=0.0, max_value=1.0, value=0.35)
rate = streamlit.radio("Choose your system type:", ["Wind Power", "Solar Power"])



if rate == "Solar Power":
    effrate = 0.35
    solartype = streamlit.radio("Please specify:", ["Water Heating Solar Power", "Non-Water Heating Solar Power"])
else:
    effrate = 0.20
    solartype = "None"


streamlit.write(f"RETC rate for {rate}: {effrate * 100}%")



proptype = streamlit.radio("Choose your property type:", ["Single Family Residential", "Multi Family Residential", "Commercial"])

if proptype == "Multi Family Residential":
    unit = streamlit.number_input("Number of units within multi faily residential: ", min_value = 2, value = 10)
else:
    unit = 0

optimized = False



if solartype == "None":
    if proptype == "Single Family Residential":
        max = 1500
    elif proptype == "Multi Family Residential":
        max = 200 * unit
    else: 
        max = 500000
elif solartype == "Water Heating Solar Power":
    if proptype == "Single Family Residential":
        max = 2250
    elif proptype == "Multi Family Residential":
        max = 350 * unit
    else: 
        max = 250000
else:
    if proptype == "Single Family Residential":
        max = 5000
    elif proptype == "Multi Family Residential":
        max = 350 * unit
    else: 
        max = 500000



cost = streamlit.number_input("Input the cost of your renewable energy system", min_value=0, value=1500)


retc = min(cost * effrate, max)
streamlit.write(f"Tax credit: ${retc}")

streamlit.write(f"Net cost: ${cost-retc}")


#optval is the optimal max value used for optretc below
if proptype == "Single Family Residential":
    optval = 5000
    bettersys = "Non-Water Heating Solar Power"
elif proptype == "Multi Family Residential":
    optval = (350 * unit)
    bettersys = "Solar Power"
else:
    optval = 500000
    bettersys = "Non-Water Heating Solar Power"

#best effective rate is 0.35 for solar always
optretc = min(cost * 0.35, optval)

#the savings is equal to the optimal retc credit value minus the actual calculated retc credit value
save = optretc - retc

if save <= 0:
    optimized = True

if optimized == True:
    streamlit.write(f"Your choice of renewable energy system ({solartype}) is optimal for your property type ({proptype}).")
else:
   streamlit.write(f"Suggestion: You can save ${save} by switching your renewable energy system to {bettersys}")

