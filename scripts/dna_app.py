import streamlit as stl
import pandas as pd
import altair as alt


def generate_sequence():
    sequence_input = ">DNA Query:\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCAGGACGGAAGGTCCTGTGCTCGGG"

    # sequence = st.sidebar.text_area("Sequence input", sequence_input, height= 250)
    sequence = stl.text_area("Sequence input:", sequence_input, height=150)
    sequence = sequence.splitlines()
    sequence = sequence[1:]  # Skip the sequence name (first line)
    sequence = ''.join(sequence)  # Concatenates list to string
    stl.write("""
    ***
    """)
    stl.subheader(f'INPUT (DNA Query)\n {sequence}')
    stl.write("""
        ***
        """)
    # DNA nucleotide Count
    stl.subheader('OUTPUT (DNA Nucleotide Count)')
    return sequence


def dna_nucleotide_count(seq):
    """Returns the count of the nucleotide sequence_input"""
    seq_dict = dict([
        ('T', seq.count('T')),
        ('A', seq.count('A')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    stl.subheader('Count in a Dictionary Form')
    stl.write(seq_dict)

    stl.subheader('Count in a Text Form')
    dna_element = seq_dict
    stl.write('There are ' + str(dna_element['T']) + ' thymine (T)')
    stl.write('There are ' + str(dna_element['A']) + ' adenine (A)')
    stl.write('There are ' + str(dna_element['G']) + ' guanine (G)')
    stl.write('There are ' + str(dna_element['C']) + ' cytosine (C)')
    return dna_element


def generate_dataframe():
    """Generates, writes and returns a dataframe"""
    dna_element = dna_nucleotide_count(generate_sequence())
    stl.subheader('Display DataFrame')
    df = pd.DataFrame.from_dict(dna_element, orient='index')
    df = df.rename({0: 'count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'nucleotide'})
    stl.write(df, use_column_width=True)
    return df


def generate_chart():
    df = generate_dataframe()
    # Display Bar Char using Altair
    stl.subheader('Display Bar Chart')
    plot_chart = alt.Chart(df).mark_bar().encode(
        x='nucleotide',
        y='count'
    )

    plot_chart = plot_chart.properties(
        width=alt.Step(80)  # Controls width of the bar.
    )
    stl.write(plot_chart)


