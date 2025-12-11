import streamlit as st

st.markdown("""
<!-- Load Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cactus+Classical+Serif&family=DM+Serif+Text:ital@0;1&family=Delius&family=Sansation:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&display=swap" rel="stylesheet">


<style>
/* H1 — Streamlit title() and markdown # */
h1 {
    font-family: "Sansation", sans-serif !important;
    font-weight: 700 !important;
    font-size: 2rem !important;
    text-align: center !important;
}

/* H2 — Streamlit header() and markdown ## */
h2 {
    font-family: "Delius", cursive !important;
    font-weight: 700 !important;
    text-align: center !important;
    font-size:1.5rem !important;
}

/* H3 — Streamlit subheader() and markdown ### */
h3 {
    font-family: "DM Serif Text", serif !important;
    font-weight: 700 !important;
    text-align: center !important
}

/* Body text font */
html, body, p, [class*="css"] {
    font-family: "Cactus Classical Serif", serif !important;
}

</style>
""", unsafe_allow_html=True)


st.title("What Are Renewable Energy Tax Credits?")


tab1, tab2, tab3, tab4 = st.tabs(["What They Are & Types", "How They Work & Eligibility", "Benefits", "How To Claim & Resources"])

with tab1:
    st.write("Renewable Energy Tax Credits (RETC’s) are dollar-for-dollar tax reductions for individuals and businesses investing in clean energy technologies and improvements. This page provides a barebones summary of tax credit options to help provide clarity. There are two key types of RETC’s: Federal and State (Hawai’i).")
    st.write("")
    st.markdown("**Federal:**")
    st.write("If you invest in energy improvements for your home, you may qualify for tax credits that cover part of the expenses. The U.S. government offers federal tax credits through the Inflation Reduction Act of 2022 by directly reducing the amount of federal income tax owed. There are two main federal tax credits available for those who make energy-related improvements to their homes:")
    st.markdown("""
        1. Residential Clean Energy Credit (RCEC)
            - If you install energy improvements to your home (like solar panels) between 2022 and 2032, you can get a federal tax credit for 30% of the cost. You can use the credit to lower your taxes, and any leftover credit can roll over to future years. Most upgrades don’t have a limit on how much credit you can claim each year, and you can claim it every year you install eligible equipment until the credit starts going down (dropping to 26% in 2033 and 22% in 2034). 
        2. Energy Efficient Home Improvement Credit
            - Similar to the RCEC, improving energy efficiency in your home qualifies you for a tax credit up to \$3,200 for work done between 2023 and 2025. There are annual limits of \$1,200 for general upgrades and \$2000 for big items like heat pumps, and you can claim the credit each year until 2025. Ultimately, if you want credit for home energy upgrades post-2025, the Residential Clean Energy Credit will be your best option. 
        """)
    st.write("")
    st.markdown("**State (Hawai’i):**")
    st.write("The Renewable Energy Technologies Income Tax Credit (RETITC) is a Hawai’i State tax credit that helps homeowners reduce the cost of installing solar or wind energy systems. This credit lowers the amount of Hawai’i state taxes you owe. If you put in solar panels, a solar hot water heater, or solar space heating, you can get back 35% of what you paid, up to a set maximum depending on your home. For most single-family houses, the cap is \$5,000 for a solar PV system and \$2,250 for a solar hot water system. If your credit is larger than the amount of state taxes you owe that year, you can roll the rest forward and use it in future years. The system must be new, installed in Hawai’i, and working during the year you claim the credit.")
    st.write("")
    st.markdown("**Types of Systems Covered:**")
    st.write("The types of new clean energy systems that qualify include:")
    st.markdown("""
        - Solar panels
        - Solar water heaters
        - Wind turbines
        - Geothermal heat pumps
        - Fuel Cells
        - Battery storage technology
    """)
    st.write("Pre-owned clean energy systems do not qualify for tax credits. There are standards for specific types listed above that must be met to qualify for the residential clean energy credit.")
    st.markdown("""
        1. __Solar water heaters:__ Must be certified by the Solar Rating Certification Corporation (SRCC) or qualified substitute approved by your state. For the state of Hawai’i, SRCC’s certifications are used in compliance with solar standards for safety.
        2. __Geothermal heat pumps:__ Must meet energy efficiency requirements established by the EPA’s Energy Star Residential New Construction program.
        3. __Battery storage technology:__ Must have a minimum capacity of 3 kilowatt hours.
    """)

with tab2:
    st.write("Tax credits for clean energy are calculated using this formula: ```system_cost * tax_credit_rate```, where system_cost is the price you paid for the installation labor and/or the clean energy technology itself, and tax_credit_rate is the percentage of your system’s cost that will be covered by credits. Multiplying the two numbers gives you the dollar value covered; for the state of Hawai’i this is 30%, so we multiply by 0.30 (the decimal form of the percentage). See the Calculator in the sidebar to try out the math!")
    st.write("Who can claim these credits? Homeowners and businesses that install new systems in Hawai’i. You can generally claim both the federal and Hawai'i state credits for the same system, but each program has its own rules, caps, and filing requirements. ")
    st.write("A quick example: if your solar PV system costs \$10,000, you might qualify for about \$3,000 in federal credit (30%) and about \$3,500 in state credit (35%). Any part of the credit that’s more than the taxes you owe may be carried forward according to each program’s rules. ")

with tab3:
    st.write("Renewable Energy Tax Credits (RETC’s) offer long-term financial and environmental benefits for Hawai’i homeowners. Installing a solar energy or water heating system can reduce both your installation costs and the amount of taxes you owe. Over time, these energy improvements lower monthly electricity bills. For many households, RETC’s make investing in clean energy systems much more affordable and help the systems pay for themselves. It’s also worth noting that homes with renewable energy upgrades may increase in property value because buyers generally value the lower energy bills and long-term savings.  ")
    st.write("Additionally, using renewable energy reduces your reliance on fossil fuels and lowers your home’s carbon footprint. This means that producing your own clean electricity helps reduce greenhouse gas emissions in Hawai’i, benefiting the community with a cleaner and healthier environment. These systems can also offer more energy independence and protection from rising electricity costs. ")

with tab4:
    st.markdown("To claim renewable energy tax credits, start with the federal Residential Clean Energy Credit using [IRS Form 5695](https://www.irs.gov/forms-pubs/about-form-5695). Make sure to keep receipts, installation records, and any certifications for your system. For Hawai’i’s [state RETITC](https://energy.hawaii.gov/income-guidelines-and-tax-resources/), use form [N-342](https://tax.hawaii.gov/forms/a1_1alphalist/) and follow state guidance for reporting costs, especially if multiple systems or owners are involved. Local installers often provide step-by-step guidance for combining federal and state credits and reputable local solar companies can provide practical instructions to ensure you claim both credits correctly and maximize your savings.")
    st.write("By following these instructions and keeping your records organized, claiming both federal and state credits can be simple, and you can make sure you receive all the savings you’re eligible for.")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown("**Information gathered from the following sources:**")
    st.markdown("[Inflation Reduction Act of 2022](https://www.irs.gov/inflation-reduction-act-of-2022)")
    st.markdown("[Home Energy Tax Credits](https://www.irs.gov/credits-deductions/home-energy-tax-credits)")
    st.markdown("[Residential Clean Energy Credit](https://www.irs.gov/credits-deductions/residential-clean-energy-credit)")
    st.markdown("[Energy Efficient Home Improvement Credit](https://www.irs.gov/credits-deductions/energy-efficient-home-improvement-credit)")
    st.markdown("[Residential Solar Electricity Benefits](https://www.energy.gov/energysaver/benefits-residential-solar-electricity)")
    st.markdown("[Renewable Energy Resources](https://energy.hawaii.gov/energy-landscape/renewable-energy-resources/)")
    
