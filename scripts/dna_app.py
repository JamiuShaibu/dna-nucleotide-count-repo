import streamlit as stl
import pandas as pd
import altair as alt


def generate_sequence():
    """Generates sequence from input"""
    sequence_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCAGGACGGAAGGTCCTGTGCTCGGG"

    stl.header('Enter DNA Sequence In The Text-Box Below...')
    sequence = stl.text_area("Clear Text-Box And Enter Sequence👇👇: E.g", sequence_input, height=150)

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
    """Writes and returns the counted elements of the nucleotide sequence_input"""
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
    stl.write(f"There are {dna_element['T']} thymine (T)")
    stl.write(f"There are {dna_element['A']} adenine (A)")
    stl.write(f"There are {dna_element['G']} guanine (G)")
    stl.write(f"There are {dna_element['C']} cytosine (C)")
    return dna_element


def generate_dataframe():
    """Generates, writes and returns a dataframe of the nucleotide sequence"""
    dna_element = dna_nucleotide_count(generate_sequence())
    stl.subheader('Display DataFrame')
    df = pd.DataFrame.from_dict(dna_element, orient='index')
    df = df.rename({0: 'Count'}, axis='columns')
    df.reset_index(inplace=True)
    df = df.rename(columns={'index': 'Nucleotide'})
    stl.write(df, use_column_width=True)
    return df


def generate_chart():
    """Generates a chart of the nucleotide positions"""
    df = generate_dataframe()
    # Display Bar Char using Altair
    stl.subheader('Display Bar Chart')
    plot_chart = alt.Chart(df).mark_bar().encode(
        x='Nucleotide',
        y='Count'
    )

    plot_chart = plot_chart.properties(
        width=alt.Step(120)
    )
    stl.write(plot_chart)


def generate_all_data():
    """Generates all computed data instructions"""
    generate_chart()



