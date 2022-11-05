# -*- coding: utf-8 -*-
"""
@author: Nik Cuculovski @Media.Monks
"""

#---------------------------------#

### import packages
from hashlib import new
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import pandas as pd
import numpy as np
import altair as alt
import random
import re
import math

from statistics import mean

#---------------------------------#

## footer
hide_menu_style = """
        <style>
        footer {visibility: hidden;}

        footer:after {
            content:'© 2022, Media.Monks. All rights reserved.';
            visibility: visible;
            display: block;
            position: relative;
            #background-color: black;
            margin-bottom:20px;
        }
        </style>
        """

### ADD PASSWORD HERE

def check_password():

    def password_entered():

        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():

### END PASSWORD HERE

    st.set_page_config(page_title="Estée Lauder - Data Center",
                        page_icon='/Users/nikolacuculovski/Desktop/PR/Pernod-Ricard-Symbol.ico',
                        layout="wide", initial_sidebar_state="expanded")

    #---------------------------------#

    ### lobby page
    def intro():

        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)

        ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        st.markdown('*The application is best viewed with the "Light" theme.'
        'If your computer is defaulted to "Dark", consider changing the calculator theme in the Settings menu found in the upper right corner.*')

        ## intro paragraph
        st.markdown("""
        # Welcome to Data Center - your custom demo platform! 👋 """)
        
        st.markdown(
            """
            Given the task to "***Deliver a hands-on-keyboard demo of how your data and technology capabilities deliver the strategic assignment and illustrate any capabilities outside the scope of the assignment that are relevant to our business***" we built a live custom demo platform to showcase some of the tools in an interactive fashion that we highlighted in our Data & Tech presentation.  While this is by no means an exhaustive list of our tools, we hope this demonstrates our capabilities as a tech first company, using technology to enable the brilliant minds at work on your business and bringing innovation back to the industry with a commitment to ongoing development of industry first solutions.
            
            To run through some of our solutions, please select a demo from the dropdown on the left to see how some of our solutions work in a live environment.

            ### Brief Tool Introduction 
            🧠 **6ix**: Positioned in the Business Context phase of the Inflection Planning process, this tool helps us store and track all of the research and insights that inform our plan.  From there, it helps us to distill critical opportunities from the noise. By scoring insights based on Business Impact, Velocity and Relevance, we are able to remove bias to ensure we are developing insights around the areas that will have the greatest impact to the assignment. 
            ***
            🧭 **Acquisition Scenario Planner (ASP)**: With rapidly changing business environments, ASP allows for quick scenario planning to understand the relationship between business factors influence performance marketing benchmarks.  This is customized to each client based on the underlying factors and patterns of their business, as well as primary KPIs.  As business factors change, or are anticipated to change, client and agency teams can see how scenarios may influence business and media KPIs and quickly make adjustments to get ahead of changing elements.
            ***
            📈 **Ad-Stock Modeling**: The effect of advertising is not immediate. Consequently, advertising ad-stock is used to measure the memory effect of advertising carried over from start of advertising.  For example, if a company advertises at a certain level in week 1, week 2 will have a portion of week 1 level. Week 3, in turn, will have a portion of week 2 level.  In other words, ad-stock is a percentage term that measures the decaying effect of advertising throughout the weeks. This tool models the ad-stock and diminishing effectiveness based on initial investment.
            ***
            🤖 **Automation & QA**: Automation of mundane repetitive tasks has a plethora of benefits. Powered by a dedicated Automation team, we have a complete suite of tools that enable us to gain operational efficiencies while reducing human error.  In addition to the key tools we’ve highlighted today, we have Citizen Automation platforms and a custom Enterprise Automation team that ensures we are continually developing new - and custom - automation tools to power our teams and partners.
            ***
            🌎 **Geo Adaptive Investment Allocation (GAIA)**: A privacy-first, cost-efficient, data and tech-agnostic framework that enables integrated location-based media planning, activation, and measurement. GAIA is a fully integrated open-source ecosystem that links influential internal and external factors to the bottomline. It provides a single view of a geo performance across all available touchpoints, it enables prioritization of resources based on incremental value, and has forward-looking capabilities that anticipate consumption habits based on historical trend, seasonality, and recent local movements.  In its current Beta form, we would use GAIA to help plan local campaign executions and analyze geo-based performance.  However, in partnership with your data team, GAIA can be expanded to serve as a hub for custom planning and measurement tools - purposely built for the retail industry.
            ***
            ⚙️ **Inflection Planning Command Center**: The Inflection Planning Dashboard is the epicenter of market intelligence and the culmination of all measurement solutions and market factors that influence how effective we are in market.  Each client’s Inflection Planning Dashboard is unique to them - based on what market factors are most important, and how their business operates.  For this version, we’ve included a “blinded” client in the Automotive space to demonstrate what an Inflection Planning Command Center might look like. 
            ***
            💡 **Media Effectiveness: MMM & MTA**: Media Mix Modeling is an econometric approach to understand high level incremental contribution of media, operations and external factors. It includes forecasting and simulation models for long-term planning and budgeting. We’ve showcased a snapshot of how our MMM and MTA solutions work.  One key differentiation for us is that we help enable brands to demystify the “black box” of MMM and MTA solutions and empower you to take whatever level of control you prefer - fully in-housed, fully managed or hybrid.
            ***
            🎼 **Screen Symphony**: Screen Symphony is our cross-screen planning, activation and measurement platform.  Leveraging a two-pronged approach (part process, part tech), we have partnered with the industry’s top players in the space and developed a custom solution that stitches together the best solution the industry has to offer.  Screen Symphony connects a unified platform across one identity solution with the largest TV data set available.  
            ***
            ⚡️ **THOR**: Majority of industry business leaders believe that data and analytics investments often only weakly relate to strategic business priorities and measurable business outcomes. THOR (Threats, Hopes, Opportunities, Rewards) is methodology that aligns business priorities to measurement investments, assesses their true Net Business Value (NBV), and helps guide future investment decisions based on a quantifiable set of outputs.
        """
        )

    #---------------------------------#

    def six_demo():

        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)

        ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        ## intro paragraph
        st.markdown("""# 🧠 Hello 6ix!  """)
        
        st.markdown(
            """
            Positioned in the Business Context phase of the Inflection Planning process, this tool helps us store and track all of the research and insights that inform our plan.  From there, it helps us to distill critical opportunities from the noise. By scoring insights based on Business Impact, Velocity and Relevance, we are able to remove bias to ensure we are developing insights around the areas that will have the greatest impact to the assignment. 
        """
        )

        ## intro paragraph
        st.markdown("""
        ***
        """)

        st.subheader("**Intelligence Input**")

        ## upload dataset
        df = st.file_uploader('Upload a list of insights here. In production versions this tool is connected to a shared Google Sheet for improved performance and centralized intelligence gathering.', type='csv', key = 'alpha')

        ### load dataset - part 1
        if df is not None:
            ### model setup
            ## read dataset
            #@st.cache(suppress_st_warning=True, allow_output_mutation=True)
            def load_data(file):
                ## read file
                df = pd.read_csv(file)
                return df

            ## load data function
            df = load_data(df)
            if df is not None:
                st.success('Dataset successfully loaded. Please review below (optional).')
            else:
                st.error('Error: End date must fall after start date.')

            st.dataframe(df)

            chart = alt.Chart(df).mark_circle().encode(
                x='Velocity Score',
                y='Business Impact Score',
                size='Relevance Score',
                color='Relevance Score',
                tooltip=['Insights','Velocity Score', 'Business Impact Score', 'Relevance Score'])

            st.subheader("**Sample Output**")
            st.markdown('One of the cornerstone outputs of 6ix.io is a matrix that identifies ares to "Protect Position", "Build Selectively", or  "Expand od Abandon" among others. Overlaying dimensions and evaluating their behaviors against each other enables Media.Monks strategist to prioritize the gathered intelligence and evalute it against percieved business impact.')

            st.text("")

            st.altair_chart(chart, use_container_width=True)

            # interactive table
            #selected_indices = st.multiselect('Select rows:', df.index)
            #selected_rows = df.loc[selected_indices]
            #st.write('### Selected Rows', selected_rows)
        
        else:
            st.info("""👆 To protect your data and privacy while demoing this prototype, please upload a .csv file first. Sample to try: [insights.csv](https://drive.google.com/file/d/1CLcuLa9oVKTYIgviryrAvgG3W0lpEZ6p/view?usp=sharing).""")

    #---------------------------------#

    def asp_demo():

        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        
        ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        ## intro paragraph
        st.markdown("""# 🧭 Hello ASP!""")
        
        st.markdown(
            """
            How can we formulate strategy in the face of uncertainty? That’s the fundamental question leaders ask as they prepare for the future. And in the midst of a global pandemic, answering it has never felt more urgent. The most recognizable tool of strategic foresight is scenario planning. It involves several stages: identifying forces that will shape future market and operating conditions; exploring how those drivers may interact; imagining a variety of plausible futures; revising mental models of the present on the basis of those futures; and then using those new models to devise strategies that prepare organizations for whatever the future actually brings.

        *\*The example below is the most simple approach and starting point that is then customized based on the client's needs.*
        """
        )

        ## intro paragraph
        st.markdown("""
        ***
        """)

        st.subheader("**Portfolio Pricing & Market Penetration**")

        personal_plus, personal_family, product_3 = st.columns(3)
        with personal_plus:
            personal_plus_pricing = st.number_input("Product 1 Cost ($): ", min_value=0, value=25, step = 1, help='Average product pricing.')
        with personal_family:
            personal_family_pricing = st.number_input("Product 2 Cost ($): ", min_value=0, value=60, step = 1, help='Average product pricing.')
        with product_3:
            product_3_pricing = st.number_input("Product 3 Cost ($): ", min_value=0, value=140, step = 1, help='Average product pricing.')

        personal_plus_people, personal_family_people, product_3_people = st.columns(3)
        with personal_plus_people:
            personal_plus_population = st.number_input("Product 1 Population (#): ", min_value=0, value=2210000, step = 1000, help='Number of product consumers.')
        with personal_family_people:
            personal_family_population = st.number_input("Product 2 Population (#): ", min_value=0, value=1250000, step = 1000, help='Number of product consumers.')
        with product_3_people:
            product_3_population = st.number_input("Product 3 Population (#): ", min_value=0, value=150000, step = 1000, help='Number of product consumers.')

        personal_plus_total = personal_plus_pricing * personal_plus_population
        personal_family_total = personal_family_pricing * personal_family_population
        personal_total = personal_plus_total + personal_family_total

        st.subheader("**Retention & Lifespan**")
        st.markdown('Industry anticipated exponential decay applied to subsequent years.')

        personal_plus_retention_y1 = st.slider('Average Frequency of Purchase per Year (#):', min_value=0, max_value=100, value=6, step=1, help='Average purchasing frequency per year per customer.')
        personal_lifetime = st.slider('Average Lifetime (#):', min_value=1, max_value=10, value=6, step=1, help='Average lifetime per consumer.')
        personal_theta_slider = st.slider('Decay Rate (Θ):', min_value=1, max_value=10, value=2, step=1, help='Average consumer decay / attrituon rate.')

        I = 1
        a = 2
        T = personal_lifetime
        dt = 1
        Nt = int(round(T/dt))                                    # no of time intervals
        u = np.zeros(Nt+1)                                       # array of u[n] values
        t = np.linspace(0, T, Nt+1)                              # time mesh                  # Backward Euler method
        theta_transform = personal_plus_retention_y1
        theta = theta_transform / personal_theta_slider

        u[0] = I                     # assign initial condition
        for n in range(0, Nt):       # n=0,1,...,Nt-1
            u[n+1] = (1 - (1-theta)*a*dt)/(1 + theta*dt*a)*u[n]
        st.line_chart(u)

        decay = pd.DataFrame(u, columns=['Decay'])

        industry_average = (((decay*personal_total).sum()[0])/(personal_plus_population+personal_family_population))/3
        industry_growth = (((decay*personal_total).sum()[0])/(personal_plus_population+personal_family_population))/4
        industry_hyper = (((decay*personal_total).sum()[0])/(personal_plus_population+personal_family_population))/5

        st.subheader("**Portfolio Acquisition Cost Targets (LTV:CAC)**")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Lifetime Value (LTV)", "$"+str(((decay*personal_total).sum()[0]/1000000000).round(2))+'B')
        col2.metric("Industry Average (3:1)", "$"+str(industry_average.round(2)))
        col3.metric("Growth (4:1)", "$"+str(industry_growth.round(2)))
        col4.metric("Hyper Growth (5:1)", "$"+str(industry_hyper.round(2)))

        st.success("Given historical and user quality trends, the optimal acquisition cost is between " + "\$"+str(industry_hyper.round(2)) + " and " + "\$"+str(industry_average.round(2)) + ".")

    #---------------------------------#

    def adstock_demo():
        
        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        
        ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        ## intro paragraph
        st.markdown("""# 📈 Hello Ad-Stock Modeling!""")
        
        st.markdown(
            """
            The effect of advertising is not immediate. Consequently, advertising ad-stock is used to measure the memory effect of advertising carried over from start of advertising.  For example, if a company advertises at a certain level in week 1, week 2 will have a portion of week 1 level. Week 3, in turn, will have a portion of week 2 level.  In other words, ad-stock is a percentage term that measures the decaying effect of advertising throughout the weeks. This tool models the ad-stock and diminishing effectiveness based on initial investment.
            
        *\*The example below is the most simple approach and starting point that is then customized based on the client's needs.*
        """
        )

        ## intro paragraph
        st.markdown("""
            ***
            """)

        ## upload dataset
        df = st.file_uploader('Upload Nielsen reach and frequency estimates here. One of Nielsen\'s limitations is that it can only estimate up to 12 impressions, and the Ad-Stock model mitigates this issue among others.', type='csv', key = 'beta')

        ### load dataset - part 1
        if df is not None:
            ### model setup
            ## read dataset
            #@st.cache(suppress_st_warning=True, allow_output_mutation=True)
            def load_data(file):
                ## read file
                df = pd.read_csv(file)
                return df

            ## load data function
            df = load_data(df)
            if df is not None:
                st.success('Dataset successfully loaded. Please review below (optional).')
            else:
                st.error('Error: End date must fall after start date.')

            with st.expander("Nielsen Exposure Data", expanded=False):
                st.table(df)

            st.subheader("**Media Inputs**")

            peak_max = max(df.iloc[:,2])
            slope_max = 1 / mean(df.iloc[:,1])
            
            #peak = st.slider('Highest Anticipated Peak of Awareness (%):', min_value=0.0, max_value=100.0, value=(peak_max*100), step=0.1, help='Average purchasing frequency per year per customer.')
            #slope = st.number_input("Product 1 Cost ($): ", min_value=0.0, value=round(slope_max*100,4), step = 0.01, help='Average product pricing.')

            new_list = []
            for i in df.iloc[:,1]:
                j = peak_max*(1-math.exp(1-math.exp(slope_max*i)))
                new_list.append(j)
            
            curve = pd.DataFrame(new_list).sort_values(by=[0], ascending=True).reset_index().drop(columns=['index'], axis=1)
            curve.columns = ['Effective Reach']

            st.line_chart(curve)

        else:
            st.info("""👆 To protect your data and privacy while demoing this prototype, please upload a .csv file first. Sample to try: [adstock.csv](https://drive.google.com/file/d/1cLhr_b7e5GODNIb0FLBVQggId_XEGl7G/view?usp=sharing).""")

    #---------------------------------#

    def asher_demo():
        
        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)
        
        ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        ## intro paragraph
        st.markdown("""# 🛠 Hello Asher!""")
        
        st.markdown(
            """
            Evaluates isolated campaign performance and identifies the point of diminishing return to establish an ideal model to inform where to invest your next dollar. Ahser is founded on Bayesian statistical inference principles with Markov Chain Monte Carlo (MCMC) sampling based on various constraints and market conditions.  While MMM and MTA is a more advanced tool to inform investment decisions, Asher is a great alternative to support brands that are either not covered in an MMM or MTA analysis, for one-off campaigns or as a supplement to MMM and MTA tools.

        *\*The example below is the most simple approach and starting point that is then customized based on the client's needs.*
        """
        )

        ## intro paragraph
        st.markdown("""
            ***
            """)

        ## upload dataset
        df = st.file_uploader('Upload Nielsen reach and frequency estimates here. One of Nielsen\'s limitations is that it can only estimate up to 12 impressions, and Asher mitigates this issue among others.', type='csv', key = 'gamma')

        ### load dataset - part 1
        if df is not None:
            ### model setup
            ## read dataset
            #@st.cache(suppress_st_warning=True, allow_output_mutation=True)
            def load_data(file):
                ## read file
                df = pd.read_csv(file)
                return df

            ## load data function
            df = load_data(df)
            if df is not None:
                st.success('Dataset successfully loaded. Please review below (optional).')
            else:
                st.error('Error: End date must fall after start date.')

            with st.expander("Nielsen Exposure Data", expanded=False):
                st.table(df)

            st.subheader("**Media Inputs**")

            a = df.iloc[:,0]
            b = df.iloc[:,1]
            log_b = np.log(df.iloc[:,1])
            coefficients = np.polyfit(df.iloc[:,0], log_b, 1)

            c = np.exp(coefficients[1]) * np.exp(coefficients[0]*df.iloc[:,1])
            
            empty_a = []
            empty_b = []
            i = 13
            for i in range(i,100):
                empty_a.append(i)
                empty_b.append((np.exp(coefficients[1]) * np.exp(coefficients[0]*i)))
                i += 1
            empty_a_arr = np.array(empty_a)
            empty_b_arr = np.array(empty_b)

            a = np.append(a, empty_a_arr)
            b = np.append(b, empty_b_arr)

            c = np.exp(coefficients[1]) * np.exp(coefficients[0]*a)

            st.line_chart(b)

            cpm, population = st.columns(2)
            with cpm:
                cpm_price = st.number_input("Weighted CPM ($): ", min_value=0.0, value=0.35, step = 0.1, help='Average cost-per-impression pricing.')
            with population:
                population_size = st.number_input("Audience Size (#): ", min_value=0, value=1300000, step = 1000, help='The size of the population being targeted.')

            cpm_final = (a*cpm_price)/10
            media_budget = ((b*population_size)*cpm_final)
            media_budget_df = pd.DataFrame(media_budget)

            df_from_arr = pd.DataFrame(data=[a, b, cpm_final, media_budget]).T

            df_from_arr.columns = ['Optimal Impressions', 'Effective Reach', 'Cost per Weighted CPM', 'Media Spend']
            df_from_arr['Cumulative Media Spend'] =  np.cumsum(df_from_arr['Media Spend'])

            slopes = df_from_arr["Effective Reach"].diff().bfill()
            signs = slopes > 0
            sign_indicator = [i for i, x in enumerate(signs) if x]

            with st.expander("Asher Optimized Data", expanded=False):
                st.table(df_from_arr.iloc[:sign_indicator[0],:])
            st.success('Given the initial constraints, the ideal effective reach is ' + str(max(df_from_arr['Optimal Impressions'][sign_indicator])) + ' impressions, with optimal cumulative media spend of  ' + "\$" +str(f'{int(round(sum(df_from_arr.iloc[:df_from_arr[df_from_arr.index.isin(sign_indicator)].index.tolist()[0],3]))):,}') + ".")

            #st.line_chart(b[::-1])

        else:
            st.info("""👆 To protect your data and privacy while demoing this prototype, please upload a .csv file first. Sample to try: [frequency.csv](https://drive.google.com/file/d/1cLhr_b7e5GODNIb0FLBVQggId_XEGl7G/view?usp=sharing).""")

    #---------------------------------#

    def automation_demo():

        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)

        ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        ## intro paragraph
        st.markdown("""# 🤖 Hello Automation and QA Tools!""")
        
        st.markdown(
            """
            We are on a mission to restore more innovation and creativity into the Media industry.  A key initiative to help us do that is our commitment to enabling Automation throughout the process.  Powered by our dedicated Automation team, we enable all employees and clients to automate critical pieces of their workflow.  Automation of mundane repetitive tasks has a plethora of benefits. A few that we think helps agencies and brands alike are:

            * Improved operational efficiency: Automation reduces time, effort and cost, whilst reducing manual errors, giving agency teams more time to focus on your primary objectives and strategic counsel.
            * Time saving: Repetitive tasks can be completed faster.
            * Improved quality and consistency: Automating processes ensures high quality results as each task is performed identically, without human error.
            * Increased employee satisfaction: Manual tasks are boring and laborious. Automation allows employees to work on more engaging activities, and thus increases satisfaction and value creation.
            * Increase customer satisfaction: Happier employees, faster processing and time savings enable teams to concentrate on providing better customer service, which all helps boost customer satisfaction.

        """
        )

        ## intro paragraph
        st.markdown("""
        ***
        """)

        st.subheader("**Tools Portfolio**")
        
        with st.expander("Data Governance", expanded=True):
            tab1, tab2, tab3 = st.tabs(["Campaign Taxonomy Builder", "Campaign Taxonomy Governance", "User Access Governance"])
        
        with tab1:
            st.markdown('### Campaign Taxonomy Builder')
            st.markdown('Establishing a global data taxonomy is the first step in effective performance reporting and media executions. Our glossary and taxonomy builder tools automate campaign naming as much as possible, while maintaining the flexibility to customize names when needed. This decreases time spent by campaign traffickers and decreases room for human error while increasing the ability to pull performance insights efficiently - no matter what team you’re on. It’s a win-win for all involved.')

        with tab2:
            st.markdown('### Campaign Taxonomy Governance')
            st.markdown('Automating taxonomy adherence governance across platforms is key to building clean data and unlocking actionable insights. After onboarding H&M and agency teams to the new taxonomy process and tool, implement an adherence plan using live dashboards, a regular communication cadence, and incentives to promote perfect compliance. This process improved a leading CPG brand’s media taxonomy compliance from 85% to 98.8% across 75+ markets.')

        with tab3:
            st.markdown('### User Access Governance')
            st.markdown('Now that your data is clean, know who has access to it at all times. H&M has already taken the first step in user access governance by centralising access requests via a support form and semi-automated ticketing system. The next step is to establish an always-on view of current users, locations, platforms, and compliance to access rules (ex: approved business domains, username taxonomy, filtered to agency/market/desired hierarchy level). Then, create email triggers that alert the relevant teams if there is a breach.')

        with st.expander("Real-Time Media Solutions", expanded=True):
            tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Inventory Operations", "Trafficking", "Campaign Creation", "Audience Creation", "Audience Onboarding", "Automated Creative Convention", "Dynamic Creatives"])
        
        with tab1:
            st.markdown('### Inventory Operations')
            st.markdown('Connect live inventory source data to update Display & Video campaign tactics in real time! For businesses who heavily rely on in stock items, our bespoke orchestrated cloud service will connect to any 3P API and monitor for updates in inventory levels then, based on logic and criteria we determine, will automatically toggle tactics based on inventory levels.Advertise the things you can sell, not what you can’t.')

        with tab2:
            st.markdown('### Trafficking')
            st.markdown('Automate your trafficking workflow. Another Media.Monks hit! MightyDesk’s trafficking tool enables media buyers to effectively scale their operations. You can make bulk edits to creatives in CM - names, dates, net new creatives, tags and more, all from a single spreadsheet and simple UI. Time savings are in the tens of thousands of hours thus far.')

        with tab3:
            st.markdown('### Campaign Creation')
            st.markdown('Linked campaign skeleton creator. Allows you to create Line Items, Placements, and Packages within CM and DV360 at the same time to maintain naming consistency across platforms.')

        with tab4:
            st.markdown('### Audience Tool')
            st.markdown('Create or edit individual or all audiences for any given CM advertiser. By entering a DCM seat ID, and a specific advertiser, you can download a google sheet template that you can use to edit existing audiences or create new ones. You can also optionally add an audience ID to edit a single audience, rather than all of them.')

        with tab5:
            st.markdown('### Audience Onboarding')
            st.markdown('Target on-boarded audiences with maximum reach across top DSPs. With custom audiences, you can reach (or exclude) the audiences most aligned with your targeting objectives. Create custom audiences using offline data such as email address, mobile device ID, last name, and postal address. Reach potential and existing customers online with display, rich media, video, and mobile campaigns. No need to have a direct contract with LiveRamp. We’ve got you covered. Pricing is CPM based and you can use the tools as much or as little as you like. Whenever you want!')

        with tab6:
            st.markdown('### Automated Creative Convetion')
            st.markdown('Efficiently update thousands of creative names. This tool is particularly useful when an Advertiser has a 1:1 relationship between creatives and targeting and there are 100s or 1000s of creatives to update at one time. This functionality is not possible within the CM UI. Google Sheets or CM API based solutions are both available.')

        with tab7:
            st.markdown('### Dynamic Creatives')
            st.markdown('Automate your creative assets. This is where the holy trinity of digital marketing comes together! Combining Data from your user’s with Technology to enable personalised communication with minimal effort. This can easily be scaled out globally and, when combined with the Worlds First Creative Dashboard your teams have full control over which creatives are being used, how they are performing and if they follow brand guidelines.')

        with st.expander("Monitoring", expanded=True):
            tab1, tab2, tab3, tab4, tab5 = st.tabs(["URLy Bird", "Campaign Monitoring Tool", "Change Rover", "Catalist", "Line Item Toggler"])
        
        with tab1:
            st.markdown('### URLy Bird')
            st.markdown('Confirm if supplied URLS are valid before launching campaigns. This spreadsheet based tool is simple and quick to use. Load all the URLs in the supplied Google sheet and run. Report any flagged URLs to your client and remove them from the serve list.')

        with tab2:
            st.markdown('### Campaign Monitoring Tool')
            st.markdown('Regularly checks and compares SDFs for anomalous settings. A Google Sheets Add-on that regularly checks, via the comparison of SDFs, that unauthorized or unexpected changes aren’t made to DV360 campaigns, insertion orders, and line items. This prevents mistakes that might lead to unauthorized expenditures from going unnoticed.')

        with tab3:
            st.markdown('### Change Rover')
            st.markdown('Autonomous DV360 Optimization Log. Change Rover is an optimization log that tracks changes across campaigns and outputs them to a-shareable log. It allows AMs to monitor all changes tracked by SDFs in campaigns, and provides clients a view-only output of all changes, dates, entities, and reasons for a change.')

        with tab4:
            st.markdown('### Catalist')
            st.markdown('Automated and recurring pivot of DV360 URL Spend report that generates URL whitelists & blacklists based on a selected KPI. Help AMs expedite the Bid Multiplying and Blocking of URLs for a given Advertiser, Insertion Order, or Line Item in DV360. Pick a date range and KPI (CTR, CPA, CPC, CPM). Get a list of potential URLs  delivered to your inbox along with the associated Spend and Conversion details.')

        with tab5:
            st.markdown('### Line Item Toggler')
            st.markdown('Automatically switches Line Items from Active/Paused using the DV360 API based on any logic needed to trigger the event. Can be used with a Dynamic Feeds. Provides functionality currently unavailable in DV360. Logic is customizable.')

    #---------------------------------#

    def datamalt_demo():
        
        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)

        ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

            ## intro paragraph
        st.markdown("""# 🌎 Hello Geo Adaptive Investment Allocation (GAIA)!""")
        
        st.markdown(
            """
        A privacy-first, cost-efficient, data and tech-agnostic framework that enables integrated location-based media planning, activation, and measurement. GAIA is a fully integrated open-source ecosystem that links influential internal and external factors to the bottomline. It provides a single view of a geo performance across all available touchpoints, it enables prioritization of resources based on incremental value, and has forward-looking capabilities that anticipate consumption habits based on historical trend, seasonality, and recent local movements.  In its current Beta form, we would use GAIA to help plan local campaign executions and analyze geo-based performance.  However, in partnership with your data team, GAIA can be expanded to serve as a hub for custom planning and measurement tools - purposely built for the retail industry.

        The solution is powered by Hexagonal Hierarchical Geospatial Indexing System (also known as H3), an open-source geospatial system built by Uber. The system uses a hexagonal grid that can be (approximately) subdivided into finer and finer hexagonal grids, combining the benefits of a hexagonal grid with S2's hierarchical subdivisions. With the largest resolution roughly the size of continents down to the smallest resolution of a meter squared, this technology gives flexibility in the size of hexagon to work with.        

        """
        )

        ## intro paragraph
        st.markdown("""
        ***
        """)

        st.subheader("**Real Life Example: GAIA in the AlcBev Industry**")
        st.markdown('*“A specific product’s success depends on one’s perception that the product will make one more attractive. Hence, the perception of attractiveness is a function of culture, society, and the purchase time frame.  Specifically, what is considered attractive in one society may vary in another. In addition, that which is considered attractive today may not be considered attractive tomorrow. Given that purchasing power parity and disposable income are the main drivers of per capita cosmetics consumption, they greatly influence purchasing habits and product success within each region.*')
        
        with st.expander("Deconstructing Consumption Habits", expanded=False):
            tab1, tab2, tab3 = st.tabs(["Culture", "Time", "Distance"])
        
        with tab1:
            st.markdown('### Culture')
            st.markdown('From country to country, spending on cosmetics varies by product type. For example, the French primarily purchase skin care products, while Germans and the British spend the most on toiletries. Compared to the EU average, Nordic countries spend a much lower share of their consumption basket on fragrances. Yet, Spain and Portugal spent lower-than-average shares on decorative cosmetics. In all those countries, metropolitan vs. rural areas also have varied differences. Demographics, family structures, migration patterns, education levels, homeownership, and proximity to choice are a few factors that impact consumer behavior. Given the cultural differences within and across the urban and rural areas across those regions, such permutations require surgically tailored marketing strategies.')

        with tab2:
            st.markdown('### Time')
            st.markdown('Conventional wisdom dictates that 80% of spending happens within a 20 mile radius. Sources such as Fortune Magazine, eBay, and Aldi among others quote this as defining investment priorities. Amplified by COVID, internet access and urbanization trends continue to redefine expectations of convenience. Recent industry research further refined those beliefs:')
            st.markdown('* 97.2% of urban consumers typically travel 20 minutes or less to make their everyday purchases.')
            st.markdown('* 70% of suburban/rural consumers will typically travel approximately more than 20 minutes for everyday purchases.')

        with tab3:
            st.markdown('### Distance')
            st.markdown('Given the differences in consumer time preferences, those parameters inform the distance how far one is willing to travel to make a purchase. In its simplest form - distance is measured through speed multiplied by time. Hence, time mean speed and space mean speed are the two representations of speed.')
            st.markdown('* With Urban average speeds of 27 mph, consumers typically can travel approximately up to 9 mile radius in 20 minutes.')
            st.markdown('* With Rural average speeds of 38 mph, consumers typically can travel approximately up to 13 mile radius in 20 minutes.')

        with st.expander("Measuring Consumption Habits", expanded=False):
            tab1, tab2, tab3 = st.tabs(["Container-based", "Spatial-based", "Distance-based"])
        
        with tab1:
            st.markdown('### Container-based')
            st.markdown('Container-based measures of alcohol outlet density are calculated based on the number of alcohol outlets in a specified area. The containers can be (a) predefined geopolitical units (e.g., cities, census tracts, DMAs, zip codes), or geographic areas defined by specific features, such as roadways; or (b) user-defined (e.g., a 1-mile buffer zone area around a local neighborhood, a 5-mile driving distance, a 5-minute driving time from a local neighborhood).')

        with tab2:
            st.markdown('### Spatial-based')
            st.markdown('Also called gravity-based measures - is based on the distances between a reference point (e.g., a high performing off-premise or on-premise center) and a selected number of alcohol outlets within a given radius. There are two types of spatial access-based measures: (1) the spatial accessibility index and (2) the population-weighted distance. This measure identifies the nodes of the network that can be found in the container.')

        with tab3:
            st.markdown('### Distance-based')
            st.markdown('To calculate alcohol outlet density as well as the edges in the network, this approach quantifies the distances between alcohol outlets—the distances between the point of critical mass based against the surrounding alcohol outlets.')
        
        st.markdown("""
        ***
        """)

        st.subheader("**Solution**")
        st.markdown('Based on the consumption habits as well as well as the measurement constructs, hexagons are the ideal solution. They do not have ambiguous neighbors, and provide uniform adjacency (decreases bias). In addition, assuming similar behavior in close proximity - hexagons can be clustered into groups and used as an aggregated value which unlocks optimization efficiencies. Depending on the on-premise and off-premise establishment density in a given hexagon, Media.Monks will have the flexibility to adjust media targeting accordingly.')
        st.markdown(' ')
        st.markdown('- The current sample protoype is supported by data.ny.gov (open-source) evaluating NYC alcohol outlets')
        st.markdown('- Each dot on the map is a registered location with the state')
        st.markdown('- The more dots in a radius, the hexagon changes color (the dataset also ranks them in 3 zones used as a validation mechanic)')
        st.markdown('- Syracuse/Rochester are interesting use-cases that show different density as compared to Manhattan')
        st.markdown('- Interesting observation - there are alochol outlets that are registered in NYC, while sell also in CA')
        st.write("")
        
        #HtmlFile = open("/Users/nikolacuculovski/Desktop/PR/kepler.gl.html", 'r', encoding='utf-8')
        #source_code = HtmlFile.read() 
        #components.html(source_code, height=700, scrolling=True)

        components.iframe("https://ncuculovski.github.io/h3/", height=700, scrolling=True)

    #---------------------------------#

    def inflection_demo():

        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)

        ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        ## intro paragraph
        st.markdown("""# ⚙️ Hello to the Inflection Planning Command Center!""")
        
        st.markdown(
            """
            Inflection Planning Command Center:  The Inflection Planning Dashboard is the epicenter of market intelligence and the culmination of all measurement solutions and market factors that influence how effective we are in market.  Each client’s Inflection Planning Dashboard is unique to them - based on what market factors are most important, and how their business operates.  For this version, we’ve included a “blinded” client in the Automotive space to demonstrate what an Inflection Planning Command Center might look like. 
            The Inflection Planning Command Center is connected to communication streams (currently supported by SMS, email and Slack notifications) to trigger teams when key Inflection Points are reached so teams can quickly respond.

            There are 3 primary components that live within the Inflection Planning Command Center:
            - Section 1: **Market Intelligence Marketplace** - Factors that have the strongest correlation to your bottom line (these are often factors we uncover via 6ix, or may be something your Advanced Analytics team already knows).  For brevity, our demo only covers this section.
            - Section 2: **Competitive Intelligence** - Analyzing and harmonizing competitive data on a regular basis, we ingest this into the dashboard and can correlate this to changes in market dynamics.  Depending on available data sets, this can include competitive media data, share of voice, competitive sales data, category brand health metrics, etc.
            - Section 3: **Media Performance Data** - Real-time media performance data, calendars of active tests, links to learning libraries and additional media information is uploaded into the dashboard as well.  Finally, since all critical Inflection Engine data may not all be available on the same schedule, we can align media performance data with marketplace factors to harmonize data on chronological order. (edited) 

        """
        )

        ## intro paragraph
        st.markdown("""
        ***
        """)

        st.subheader("**Intelligence Output**")

        ## upload dataset
        df = st.file_uploader('Upload a list of insights here. In production versions this tool is connected to a shared Google Sheet for improved performance and centralized intelligence gathering.', type='csv', key = 'theta')

        ### load dataset - part 1
        if df is not None:
            ### model setup
            ## read dataset
            #@st.cache(suppress_st_warning=True, allow_output_mutation=True)
            def load_data(file):
                ## read file
                df = pd.read_csv(file)
                return df

            ## load data function
            df = load_data(df)
            if df is not None:
                st.success('Dataset successfully loaded. Please review below (optional).')
            else:
                st.error('Error: End date must fall after start date.')

            #df = pd.read_csv('/Users/nikolacuculovski/Desktop/PR/inflection.csv')
            df.iloc[:,0] = pd.to_datetime(df.iloc[:,0])
            df.iloc[:,1:] = df.iloc[:,1:].astype(float)
            with st.expander("Inflection Data", expanded=False):
                st.dataframe(df)

            st.write("")

            ## write image
            col1, col2, col3 = st.columns([3,3,3])
            with col1:
                with st.expander("Business Category", expanded=True):
                    tab1, tab2 = st.tabs(["Dow Jones Industrial Average (DJIA)", " "])
                    with tab1:
                        st.line_chart(df.iloc[:,21:22])
            with col2:
                with st.expander("Business Category", expanded=True):
                    tab1, tab2 = st.tabs(["CBOE Volatility Index (IXIC)", " "])
                    with tab1:
                        st.line_chart(df.iloc[:,39:40])
            with col3:
                with st.expander("Business Category", expanded=True):
                    tab1, tab2 = st.tabs(["Case Shiller Home Price Index", " "])
                    with tab1:
                        st.line_chart(df.iloc[:,7:8])

            col1, col2, col3 = st.columns([3,3,3])
            with col1:
                with st.expander("Consumer Category", expanded=True):
                    tab1, tab2 = st.tabs(["Gasoline Prices", " "])
                    with tab1:
                        st.line_chart(df.iloc[:,30:31])
            with col2:
                with st.expander("Consumer Category", expanded=True):
                    tab1, tab2 = st.tabs(["Consumer Confidence", " "])
                    with tab1:
                        st.line_chart(df.iloc[:,11:12])
            with col3:
                with st.expander("Consumer Category", expanded=True):
                    tab1, tab2 = st.tabs(["Unemployment Rate", " "])
                    with tab1:
                        st.line_chart(df.iloc[:,59:60])

            df = df.iloc[: , 1:]

            def normalize(df):
                result = df.copy()
                for feature_name in df.columns:
                    max_value = df[feature_name].max()
                    min_value = df[feature_name].min()
                    result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
                return result
            df = normalize(df)

            ## write image
            st.subheader("**Factor Evaluation**")

            options = st.multiselect("",df.columns.to_list(), ['consumer_confidence', 'core_inflation_rate', 'gasoline_prices'])
            if len(options) > 0:
                st.dataframe(df[options].corr(method='pearson'), width=1200)
                st.area_chart(df[options], height=470)

            col1, col2 = st.columns([1.5,3])
            with col1:
                option_1 = st.selectbox('Independent Variable', df.columns.to_list(), key = 1)
                option_2 = st.selectbox('Dependent Variable', df.columns.to_list(), key = 2)
                corr_2 = df[option_1].corr(df[option_2])
                if corr_2 > 0:
                    st.success('The correlation coefficient between both variables is ' + str(round(corr_2,2)) + '.')
                else:
                    st.error('The correlation coefficient between both variables is ' + str(round(corr_2,2)) + '.')

                st.vega_lite_chart(df, {
                    'mark': {'type': 'circle', 'tooltip': True},
                    'encoding': {
                        'x': {'field': option_1, 'type': 'quantitative'},
                        'y': {'field': option_2, 'type': 'quantitative'},
                        'size': {'field': option_2, 'type': 'quantitative'},
                        'color': {'field': option_2, 'type': 'quantitative'},
                    },
                }, use_container_width = True)

            with col2:
                merger = pd.merge(df[option_1], df[option_2], right_index = True, left_index = True)
                st.bar_chart(merger, height = 650)

        else:
            st.info("""👆 To protect your data and privacy while demoing this prototype, please upload a .csv file first. Sample to try: [inflection.csv](https://drive.google.com/file/d/1gNTCes61APBa08xb-8b1SihhOnKMX6ud/view?usp=sharing).""")

    #---------------------------------#

    def mmm_demo():
        ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)

    ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        ## intro paragraph
        st.markdown("""# 💡 Hello Media Effectiveness: MTA & MMM!""")
        
        st.markdown(
            """
            Media Mix Modeling is an econometric approach to understand high level incremental contribution of media, operations and external factors. It includes forecasting and simulation models for long-term planning and budgeting. We’ve showcased a snapshot of how our MMM and MTA solutions work.  One key differentiation for us is that we help enable brands to demystify the “black box” of MMM and MTA solutions and empower you to take whatever level of control you prefer - fully in-housed, fully managed or hybrid.
        """
        )

        st.info("""👆 To access our proprietary platform, please [click here](https://reports.brightblueconsulting.co.uk/).""")

    #---------------------------------#

    def thor_demo():

    ## add footer
        st.markdown(hide_menu_style, unsafe_allow_html=True)

    ## import image
        image = Image.open('logo.png')
        ## write image
        col1, col2, col3 = st.columns([1.5,3,1.5])
        with col1:
            st.write("")
        with col2:
            st.image(image, width=650, use_column_width=True)
        with col3:
            st.write("")

        ## intro paragraph
        st.markdown("""
        ***
        """)

        ## intro paragraph
        st.markdown("""# ⚡️ Hello THOR!""")
        
        st.markdown(
            """
            Majority of industry business leaders believe that data and analytics investments often only weakly relate to strategic business priorities and measurable business outcomes. THOR (Threats, Hopes, Opportunities, Rewards) is methodology that aligns business priorities to measurement investments, assesses their true Net Business Value (NBV), and helps guide future investment decisions based on a quantifiable set of outputs.

            Traditional investment tools such as NPV, IRR, PI, and ROI are commonly used and valuable, but have some challenges if used independently:
            - Siloed investment evaluation
            - Implicit product assumptions and required effort
            - Risk and capability gaps are hidden
            - Oversimplification rating of ROI and investments

            THOR is a complementary strategic model that aims to assess, prioritize, and quantify the value and risk of analytics solution investments that target the business priorities. The model explicitly identifies foundational gaps in data, technology, and organizational capability that are necessary conditions for successful solution delivery. 
            
            Also, THOR is a deterministic quantitative model that provides one possible output for a given set of unique inputs. It uses up to 120 questions segmented in 6 dimensions to balance any potential bias introduced by the appraiser.

            *\*For simplicity, the evaluation criteria is simplified and common analytical products are evaluated only as an example.*

        """
        )

        ## intro paragraph
        st.markdown("""
        ***
        """)

        st.subheader("**Intelligence Input**")
        
        with st.expander("Evaluation Criteria", expanded=False):
            tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Media Mix Modelling", "Multi-Touch Attribution", "Uplift Modelling", "Forecasting", "GAIA", "Last-Touch Attribution"])
        with tab1:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('### Value')
                pr1_revenue_growth = st.radio("Revenue growth impact",(1, 2, 3, 4, 5), index=3, key = 1)
                pr1_critical_business = st.radio("Support for critical business initiatives",(1, 2, 3, 4, 5), index=4, key = 2)
                pr1_business_impact = st.radio("Cost optimization and market responsiveness",(1, 2, 3, 4, 5), index=3, key = 3)
            with col2:
                st.markdown('### Organization')
                org1_ability = st.radio("Measure success and business impact",(1, 2, 3, 4, 5), index=3, key = 4)
                org1_key_initiatives = st.radio("Alignment with business initiatives",(1, 2, 3, 4, 5), index=3, key = 5)
                org1_decision_complexity = st.radio("Decision complexity",(1, 2, 3, 4, 5), index=2, key = 6)
            with col3:
                st.markdown('### Growth')
                gr1_ability = st.radio("Links KPIs to corporate objectives",(1, 2, 3, 4, 5), index=4, key = 7)
                gr1_key_initiatives = st.radio("Available to users with lower skills",(1, 2, 3, 4, 5), index=3, key = 8)
                gr1_decision_complexity = st.radio("Adapt to changing requirements",(1, 2, 3, 4, 5), index=3, key = 9)

            col4, col5, col6 = st.columns(3)
            with col4:
                st.markdown('### Data')
                dt1_value_prop = st.radio("Proposal matches value proposition",(1, 2, 3, 4, 5), index=2, key = 10)
                dt1_bias = st.radio("Varied and complete to mitigate bias",(1, 2, 3, 4, 5), index=2, key = 11)
                dt1_reuse = st.radio("Reuse across other value propositions",(1, 2, 3, 4, 5), index=3, key = 12)
            with col5:
                st.markdown('### Technology')
                tc1_ability = st.radio("Business impact if data is wrong",(1, 2, 3, 4, 5), index=0, key = 13)
                tc1_key_initiatives = st.radio("Technology scalability",(1, 2, 3, 4, 5), index=0, key = 14)
                tc1_decision_complexity = st.radio("Well scoped and understood",(1, 2, 3, 4, 5), index=2, key = 15)
            with col6:
                st.markdown('### Cost')
                cs1_ability = st.radio("Confidence in assumptions",(1, 2, 3, 4, 5), index=4, key = 16)
                cs1_key_initiatives = st.radio("Data management infrastructure",(1, 2, 3, 4, 5), index=1, key = 17)
                cs1_decision_complexity = st.radio("Enhances analytics workbench",(1, 2, 3, 4, 5), index=3, key = 18)

        with tab2:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('### Value')
                pr2_revenue_growth = st.radio("Revenue growth impact",(1, 2, 3, 4, 5), index=2, key = 19)
                pr2_critical_business = st.radio("Support for critical business initiatives",(1, 2, 3, 4, 5), index=2, key = 20)
                pr2_business_impact = st.radio("Business Impact Metrics Definition",(1, 2, 3, 4, 5), index=1, key = 21)
            with col2:
                st.markdown('### Organization')
                org2_ability = st.radio("Measure success and business impact",(1, 2, 3, 4, 5), index=2, key = 22)
                org2_key_initiatives = st.radio("Alignment with business initiatives",(1, 2, 3, 4, 5), index=4, key = 23)
                org2_decision_complexity = st.radio("Decision complexity",(1, 2, 3, 4, 5), index=3, key = 24)
            with col3:
                st.markdown('### Growth')
                gr2_ability = st.radio("Links KPIs to corporate objectives",(1, 2, 3, 4, 5), index=1, key = 25)
                gr2_key_initiatives = st.radio("Available to users with lower skills",(1, 2, 3, 4, 5), index=2, key = 26)
                gr2_decision_complexity = st.radio("Adapt to changing requirements",(1, 2, 3, 4, 5), index=2, key = 27)

            col4, col5, col6 = st.columns(3)
            with col4:
                st.markdown('### Data')
                dt2_value_prop = st.radio("Proposal matches value proposition",(1, 2, 3, 4, 5), index=3, key = 28)
                dt2_bias = st.radio("Varied and complete to mitigate bias",(1, 2, 3, 4, 5), index=2, key = 29)
                dt2_reuse = st.radio("Reuse across other value propositions",(1, 2, 3, 4, 5), index=1, key = 30)
            with col5:
                st.markdown('### Technology')
                tc2_ability = st.radio("Business impact if data is wrong",(1, 2, 3, 4, 5), index=2, key = 31)
                tc2_key_initiatives = st.radio("Technology scalability",(1, 2, 3, 4, 5), index=4, key = 32)
                tc2_decision_complexity = st.radio("Well scoped and understood",(1, 2, 3, 4, 5), index=3, key = 33)
            with col6:
                st.markdown('### Cost')
                cs2_ability = st.radio("Confidence in assumptions",(1, 2, 3, 4, 5), index=2, key = 34)
                cs2_key_initiatives = st.radio("Data management infrastructure",(1, 2, 3, 4, 5), index=2, key = 35)
                cs2_decision_complexity = st.radio("Enhances analytics workbench",(1, 2, 3, 4, 5), index=2, key = 36)

        with tab3:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('### Value')
                pr3_revenue_growth = st.radio("Revenue growth impact",(1, 2, 3, 4, 5), index=0, key = 37)
                pr3_critical_business = st.radio("Support for critical business initiatives",(1, 2, 3, 4, 5), index=0, key = 38)
                pr3_business_impact = st.radio("Business Impact Metrics Definition",(1, 2, 3, 4, 5), index=2, key = 39)
            with col2:
                st.markdown('### Organization')
                org3_ability = st.radio("Measure success and business impact",(1, 2, 3, 4, 5), index=1, key = 40)
                org3_key_initiatives = st.radio("Alignment with business initiatives",(1, 2, 3, 4, 5), index=3, key = 41)
                org3_decision_complexity = st.radio("Decision complexity",(1, 2, 3, 4, 5), index=2, key = 42)
            with col3:
                st.markdown('### Growth')
                gr3_ability = st.radio("Links KPIs to corporate objectives",(1, 2, 3, 4, 5), index=3, key = 43)
                gr3_key_initiatives = st.radio("Available to users with lower skills",(1, 2, 3, 4, 5), index=3, key = 44)
                gr3_decision_complexity = st.radio("Adapt to changing requirements",(1, 2, 3, 4, 5), index=3, key = 45)

            col4, col5, col6 = st.columns(3)
            with col4:
                st.markdown('### Data')
                dt3_value_prop = st.radio("Proposal matches value proposition",(1, 2, 3, 4, 5), index=2, key = 46)
                dt3_bias = st.radio("Varied and complete to mitigate bias",(1, 2, 3, 4, 5), index=2, key = 47)
                dt3_reuse = st.radio("Reuse across other value propositions",(1, 2, 3, 4, 5), index=2, key = 48)
            with col5:
                st.markdown('### Technology')
                tc3_ability = st.radio("Business impact if data is wrong",(1, 2, 3, 4, 5), index=1, key = 49)
                tc3_key_initiatives = st.radio("Technology scalability",(1, 2, 3, 4, 5), index=2, key = 50)
                tc3_decision_complexity = st.radio("Well scoped and understood",(1, 2, 3, 4, 5), index=2, key = 51)
            with col6:
                st.markdown('### Cost')
                cs3_ability = st.radio("Confidence in assumptions",(1, 2, 3, 4, 5), index=1, key = 52)
                cs3_key_initiatives = st.radio("Data management infrastructure",(1, 2, 3, 4, 5), index=1, key = 53)
                cs3_decision_complexity = st.radio("Enhances analytics workbench",(1, 2, 3, 4, 5), index=2, key = 54)

        with tab4:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('### Value')
                pr4_revenue_growth = st.radio("Revenue growth impact",(1, 2, 3, 4, 5), index=0, key = 55)
                pr4_critical_business = st.radio("Support for critical business initiatives",(1, 2, 3, 4, 5), index=0, key = 56)
                pr4_business_impact = st.radio("Business Impact Metrics Definition",(1, 2, 3, 4, 5), index=2, key = 57)
            with col2:
                st.markdown('### Organization')
                org4_ability = st.radio("Measure success and business impact",(1, 2, 3, 4, 5), index=0, key = 58)
                org4_key_initiatives = st.radio("Alignment with business initiatives",(1, 2, 3, 4, 5), index=1, key = 59)
                org4_decision_complexity = st.radio("Decision complexity",(1, 2, 3, 4, 5), index=2, key = 60)
            with col3:
                st.markdown('### Growth')
                gr4_ability = st.radio("Links KPIs to corporate objectives",(1, 2, 3, 4, 5), index=1, key = 61)
                gr4_key_initiatives = st.radio("Available to users with lower skills",(1, 2, 3, 4, 5), index=2, key = 62)
                gr4_decision_complexity = st.radio("Adapt to changing requirements",(1, 2, 3, 4, 5), index=0, key = 63)

            col4, col5, col6 = st.columns(3)
            with col4:
                st.markdown('### Data')
                dt4_value_prop = st.radio("Proposal matches value proposition",(1, 2, 3, 4, 5), index=3, key = 64)
                dt4_bias = st.radio("Varied and complete to mitigate bias",(1, 2, 3, 4, 5), index=3, key = 65)
                dt4_reuse = st.radio("Reuse across other value propositions",(1, 2, 3, 4, 5), index=3, key = 66)
            with col5:
                st.markdown('### Technology')
                tc4_ability = st.radio("Business impact if data is wrong",(1, 2, 3, 4, 5), index=1, key = 67)
                tc4_key_initiatives = st.radio("Technology scalability",(1, 2, 3, 4, 5), index=4, key = 68)
                tc4_decision_complexity = st.radio("Well scoped and understood",(1, 2, 3, 4, 5), index=2, key = 69)
            with col6:
                st.markdown('### Cost')
                cs4_ability = st.radio("Confidence in assumptions",(1, 2, 3, 4, 5), index=1, key = 70)
                cs4_key_initiatives = st.radio("Data management infrastructure",(1, 2, 3, 4, 5), index=1, key = 71)
                cs4_decision_complexity = st.radio("Enhances analytics workbench",(1, 2, 3, 4, 5), index=2, key = 72)

        with tab5:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('### Value')
                pr5_revenue_growth = st.radio("Revenue growth impact",(1, 2, 3, 4, 5), index=0, key = 73)
                pr5_critical_business = st.radio("Support for critical business initiatives",(1, 2, 3, 4, 5), index=0, key = 74)
                pr5_business_impact = st.radio("Business Impact Metrics Definition",(1, 2, 3, 4, 5), index=1, key = 75)
            with col2:
                st.markdown('### Organization')
                org5_ability = st.radio("Measure success and business impact",(1, 2, 3, 4, 5), index=0, key = 76)
                org5_key_initiatives = st.radio("Alignment with business initiatives",(1, 2, 3, 4, 5), index=3, key = 77)
                org5_decision_complexity = st.radio("Decision complexity",(1, 2, 3, 4, 5), index=3, key = 78)
            with col3:
                st.markdown('### Growth')
                gr5_ability = st.radio("Links KPIs to corporate objectives",(1, 2, 3, 4, 5), index=4, key = 79)
                gr5_key_initiatives = st.radio("Available to users with lower skills",(1, 2, 3, 4, 5), index=1, key = 80)
                gr5_decision_complexity = st.radio("Adapt to changing requirements",(1, 2, 3, 4, 5), index=0, key = 81)

            col4, col5, col6 = st.columns(3)
            with col4:
                st.markdown('### Data')
                dt5_value_prop = st.radio("Proposal matches value proposition",(1, 2, 3, 4, 5), index=2, key = 82)
                dt5_bias = st.radio("Varied and complete to mitigate bias",(1, 2, 3, 4, 5), index=2, key = 83)
                dt5_reuse = st.radio("Reuse across other value propositions",(1, 2, 3, 4, 5), index=2, key = 84)
            with col5:
                st.markdown('### Technology')
                tc5_ability = st.radio("Business impact if data is wrong",(1, 2, 3, 4, 5), index=0, key = 85)
                tc5_key_initiatives = st.radio("Technology scalability",(1, 2, 3, 4, 5), index=1, key = 86)
                tc5_decision_complexity = st.radio("Well scoped and understood",(1, 2, 3, 4, 5), index=2, key = 87)
            with col6:
                st.markdown('### Cost')
                cs5_ability = st.radio("Confidence in assumptions",(1, 2, 3, 4, 5), index=2, key = 88)
                cs5_key_initiatives = st.radio("Data management infrastructure",(1, 2, 3, 4, 5), index=2, key = 89)
                cs5_decision_complexity = st.radio("Enhances analytics workbench",(1, 2, 3, 4, 5), index=2, key = 90)

        with tab6:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('### Value')
                pr6_revenue_growth = st.radio("Revenue growth impact",(1, 2, 3, 4, 5), index=0, key = 91)
                pr6_critical_business = st.radio("Support for critical business initiatives",(1, 2, 3, 4, 5), index=0, key = 92)
                pr6_business_impact = st.radio("Business Impact Metrics Definition",(1, 2, 3, 4, 5), index=0, key = 93)
            with col2:
                st.markdown('### Organization')
                org6_ability = st.radio("Measure success and business impact",(1, 2, 3, 4, 5), index=0, key = 94)
                org6_key_initiatives = st.radio("Alignment with business initiatives",(1, 2, 3, 4, 5), index=0, key = 95)
                org6_decision_complexity = st.radio("Decision complexity",(1, 2, 3, 4, 5), index=1, key = 96)
            with col3:
                st.markdown('### Growth')
                gr6_ability = st.radio("Links KPIs to corporate objectives",(1, 2, 3, 4, 5), index=0, key = 97)
                gr6_key_initiatives = st.radio("Available to users with lower skills",(1, 2, 3, 4, 5), index=1, key = 98)
                gr6_decision_complexity = st.radio("Adapt to changing requirements",(1, 2, 3, 4, 5), index=0, key = 99)

            col4, col5, col6 = st.columns(3)
            with col4:
                st.markdown('### Data')
                dt6_value_prop = st.radio("Proposal matches value proposition",(1, 2, 3, 4, 5), index=0, key = 100)
                dt6_bias = st.radio("Varied and complete to mitigate bias",(1, 2, 3, 4, 5), index=0, key = 101)
                dt6_reuse = st.radio("Reuse across other value propositions",(1, 2, 3, 4, 5), index=2, key = 102)
            with col5:
                st.markdown('### Technology')
                tc6_ability = st.radio("Business impact if data is wrong",(1, 2, 3, 4, 5), index=0, key = 103)
                tc6_key_initiatives = st.radio("Technology scalability",(1, 2, 3, 4, 5), index=1, key = 104)
                tc6_decision_complexity = st.radio("Well scoped and understood",(1, 2, 3, 4, 5), index=2, key = 105)
            with col6:
                st.markdown('### Cost')
                cs6_ability = st.radio("Confidence in assumptions",(1, 2, 3, 4, 5), index=1, key = 106)
                cs6_key_initiatives = st.radio("Data management infrastructure",(1, 2, 3, 4, 5), index=1, key = 107)
                cs6_decision_complexity = st.radio("Enhances analytics workbench",(1, 2, 3, 4, 5), index=2, key = 108)


        with st.expander("Risk Tolerance", expanded=False):
            longterm_value = st.slider('Longterm Value %', 0, 100, 75)
            risk = st.slider('Acceptable risk %', 0, 100, 45)


        ## product 2
        pr1_value_avg = (pr1_revenue_growth + pr1_critical_business + pr1_business_impact) /3 
        pr1_org_avg = (org1_ability + org1_key_initiatives + org1_decision_complexity) / 3
        pr1_gr_avg = (gr1_ability + gr1_key_initiatives + gr1_decision_complexity) / 3
        pr1_positive = (pr1_value_avg + pr1_org_avg + pr1_gr_avg) * ((longterm_value)/100)
        
        pr1_data_avg = (dt1_value_prop + dt1_bias + dt1_reuse) / 3
        pr1_tech_avg = (tc1_ability + tc1_key_initiatives + tc1_decision_complexity) / 3
        pr1_cost_avg = (cs1_ability + cs1_key_initiatives + cs1_decision_complexity) / 3
        pr1_negative = pr1_data_avg + pr1_tech_avg + pr1_cost_avg * ((risk)/100)
        
        ## product 2
        pr2_value_avg = (pr2_revenue_growth + pr2_critical_business + pr2_business_impact) /3 
        pr2_org_avg = (org2_ability + org2_key_initiatives + org2_decision_complexity) / 3
        pr2_gr_avg = (gr2_ability + gr2_key_initiatives + gr2_decision_complexity) / 3
        pr2_positive = pr2_value_avg + pr2_org_avg + pr2_gr_avg * ((longterm_value)/100)
        
        pr2_data_avg = (dt2_value_prop + dt2_bias + dt2_reuse) / 3
        pr2_tech_avg = (tc2_ability + tc2_key_initiatives + tc2_decision_complexity) / 3
        pr2_cost_avg = (cs2_ability + cs2_key_initiatives + cs2_decision_complexity) / 3
        pr2_negative = pr2_data_avg + pr2_tech_avg + pr2_cost_avg * ((risk)/100)

        ## product 3
        pr3_value_avg = (pr3_revenue_growth + pr3_critical_business + pr3_business_impact) /3 
        pr3_org_avg = (org3_ability + org3_key_initiatives + org3_decision_complexity) / 3
        pr3_gr_avg = (gr3_ability + gr3_key_initiatives + gr3_decision_complexity) / 3
        pr3_positive = pr3_value_avg + pr3_org_avg + pr3_gr_avg * ((longterm_value)/100)
        
        pr3_data_avg = (dt3_value_prop + dt3_bias + dt3_reuse) / 3
        pr3_tech_avg = (tc3_ability + tc3_key_initiatives + tc3_decision_complexity) / 3
        pr3_cost_avg = (cs3_ability + cs3_key_initiatives + cs3_decision_complexity) / 3
        pr3_negative = pr3_data_avg + pr3_tech_avg + pr3_cost_avg * ((risk)/100)

        ## product 4
        pr4_value_avg = (pr4_revenue_growth + pr4_critical_business + pr4_business_impact) /3 
        pr4_org_avg = (org4_ability + org4_key_initiatives + org4_decision_complexity) / 3
        pr4_gr_avg = (gr4_ability + gr4_key_initiatives + gr4_decision_complexity) / 3
        pr4_positive = pr4_value_avg + pr4_org_avg + pr4_gr_avg * ((longterm_value)/100)
        
        pr4_data_avg = (dt4_value_prop + dt4_bias + dt4_reuse) / 3
        pr4_tech_avg = (tc4_ability + tc4_key_initiatives + tc4_decision_complexity) / 3
        pr4_cost_avg = (cs4_ability + cs4_key_initiatives + cs4_decision_complexity) / 3
        pr4_negative = pr4_data_avg + pr4_tech_avg + pr3_cost_avg * ((risk)/100)

        ## product 5
        pr5_value_avg = (pr5_revenue_growth + pr5_critical_business + pr5_business_impact) /3 
        pr5_org_avg = (org5_ability + org5_key_initiatives + org5_decision_complexity) / 3
        pr5_gr_avg = (gr5_ability + gr5_key_initiatives + gr5_decision_complexity) / 3
        pr5_positive = pr5_value_avg + pr5_org_avg + pr5_gr_avg * ((longterm_value)/100)
        
        pr5_data_avg = (dt5_value_prop + dt5_bias + dt5_reuse) / 3
        pr5_tech_avg = (tc5_ability + tc5_key_initiatives + tc5_decision_complexity) / 3
        pr5_cost_avg = (cs5_ability + cs5_key_initiatives + cs5_decision_complexity) / 3
        pr5_negative = pr5_data_avg + pr5_tech_avg + pr3_cost_avg * ((risk)/100)

        ## product 6
        pr6_value_avg = (pr6_revenue_growth + pr6_critical_business + pr6_business_impact) /3 
        pr6_org_avg = (org6_ability + org6_key_initiatives + org6_decision_complexity) / 3
        pr6_gr_avg = (gr6_ability + gr6_key_initiatives + gr6_decision_complexity) / 3
        pr6_positive = pr6_value_avg + pr6_org_avg + pr6_gr_avg * ((longterm_value)/100)
        
        pr6_data_avg = (dt6_value_prop + dt6_bias + dt6_reuse) / 3
        pr6_tech_avg = (tc6_ability + tc6_key_initiatives + tc6_decision_complexity) / 3
        pr6_cost_avg = (cs6_ability + cs6_key_initiatives + cs6_decision_complexity) / 3
        pr6_negative = pr6_data_avg + pr6_tech_avg + pr3_cost_avg * ((risk)/100)

        thor_data = [['Media Mix Modelling', pr1_positive, pr1_negative], ['Multi-Touch Attribution', pr2_positive, pr2_negative], ['Uplift Modelling', pr3_positive, pr3_negative], ['Forecasting', pr4_positive, pr4_negative], ['GAIA', pr5_positive, pr5_negative], ['Last-Touch Attribution', pr6_positive, pr6_negative]]
        thor_df = pd.DataFrame(thor_data, columns=['Product Name', 'Reward', 'Risk'])

        chart2 = alt.Chart(thor_df).mark_circle().encode(
                    x='Reward',
                    y='Risk',
                    size='Reward',
                    #color='Positive',
                    tooltip=['Product Name', 'Reward', 'Risk'])

        st.subheader("**Sample Output**")
        st.markdown('One of the cornerstone outputs of 6ix.io is a matrix that identifies ares to "Protect Position", "Build Selectively", or  "Expand od Abandon" among others. Overlaying dimensions and evaluating their behaviors against each other enables Media.Monks strategist to prioritize the gathered intelligence and evalute it against percieved business impact.')

        st.text("")

        st.altair_chart(chart2, use_container_width=True)

    #---------------------------------#

    page_names_to_funcs = {
        "Home": intro,
        "6ix": six_demo,
        "Acquisition Scenario Planner": asp_demo,
        "Ad-Stock Modeling": adstock_demo,
        "Asher Optimizer": asher_demo,
        "Automation & QA": automation_demo,
        "GAIA": datamalt_demo,
        "Inflection Planning Dashboard": inflection_demo,
        "Media Effectiveness: MTA & MMM": mmm_demo,
        "THOR": thor_demo,
    }

    #---------------------------------#

    st.sidebar.header('Estée Lauder Sample Data Tools')
    demo_name = st.sidebar.selectbox("Please choose a tool to demo", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()