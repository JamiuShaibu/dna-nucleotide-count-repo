import streamlit as stl


def get_text_content():
    """Holds explanatory information"""
    stl.markdown(
        "<h5 style='text-align: center; color: navy;'>Simple and Brief Explanation of Nucleotide and it's Bases</h5>",
        unsafe_allow_html=True)
    with stl.expander("Read more content here"):
        stl.write("""**What is a Nucleotide?**\n ***Nucleotides*** are organic molecules that serve as the basic structural (
monomer) units for DNA and RNA, which, as we know, are the building blocks responsible for all life on Earth. 

Each nucleotide contains a nitrogenous base, a five-carbon sugar, and at least one phosphate group. When bonded 
together, nucleotides create nucleic acid, that is, the "strings" of DNA. 

Nucleotides can also stand independently and interact with cells in other ways.


**what is a Nucleotide Structure?** We know that nucleotides are the building blocks of DNA and RNA, but they also do 
a lot of other things. In order to understand why and how nucleotides perform their extremely important jobs, 
let's first go over what they're made out of and how they become nucleic acid. 


**Nucleotide Bases**

**Bases** are the part of DNA that stores information and gives DNA the ability to encode phenotype, a person’s 
visible traits. Adenine and guanine are purine bases. These are structures composed of a 5-sided and 6-sided ring. 
Cytosine and thymine are pyrimidines which are structures composed of a single six-sided ring. Adenine always binds 
to thymine, while cytosine and guanine always bind to one another. This relationship is called complementary base 
paring. These complementary bases are bonded together via hydrogen bonds, which can be easily broken apart when the 
DNA needs to unzip and duplicate itself. 


The type of nucleotide is defined by its chemical base. There are four chemical bases:

1. Thymine (T)
2. Adenine (A)
3. Guanine (G)
4. Cytosine (C)\n

**The base and the amount of phosphate residue define how the compound is named.** For example, an Adenine nucleotide 
with one phosphate group is called adenosine monophosphate. "Adenosine" refers to "Adenine," or the chemical base of 
the nucleotide, and "monophosphate" refers to the fact that it has one phosphate group (remember that "mono" means 
"one"!). 

These bases are each defined by a letter and are either ***pyrimidines or purines.***\n

**Thymine (T):** Thymine is a pyrimidine with the chemical compound C5H6N2O2. A thymine-based nucleotide is called a 
thymidine. Thymine is a fused ring with conjugated bonds. Thymine bonds with adenine to form nucleic acid; this helps 
stabilize the nucleic acid structures. 

**Adenine (A):** Adenine is a purine with the chemical compound C5H5N5. An Adenine-based nucleotide is called 
adenosine. Adenine is formed by two hydrogen bonds, which help stabilize nucleic acid structures. ATP (adenosine 
triphosphate) is also an important form of energy, found in most cellular functions.\n 

**Guanine (G):** Guanine is a purine with the chemical compound C5H5N5O. A guanine-based nucleotide is called a 
guanosine. Guanine is a fused ring with conjugated double bonds. Guanine bonds with cytosine via three hydrogen bonds 
to form the nucleic acid in DNA.\n 

**Cytosine (C):** Cytosine is a pyrimidine with the chemical compound C4H5N3O. A cytosine-based nucleotide is called 
a cytosine. Cytosine is a heterocyclic aromatic ring with two substituents attached. Cytosine pairs with guanine to 
form nucleic acid, but as a free nucleotide can work as a co-enzyme that helps convert ADP (adenosine diphosphate) to 
ATP. 

**Note;>>> Uracil (U):** Uracil is a weak acid with the chemical compound C4H4N2O2. A uracil-based nucleotide is 
called uridine. ***Uracil is a demethylated form of thymine,*** and ***replaces thymine in RNA.*** Demethylation is a 
chemical process in the removal of CH3 (or a methyl group) from a molecule. 

The bases can combine with phosphates and sugars depending on how they're formed, and serve as free nucleotides, 
in which they affect cell function. Or these nucleotides can bond with one another based on their molecular 
structures to form nucleic acid. 

""")

    stl.markdown('''<h5 style='text-align: center; color: navy'>CONCLUSION</h5>
<p style='text-align: center'><strong>What is a Nucleotide? How Do They Work?</strong> Nucleotides are just one part of 
the intricate world of cellular biology. They play a central role in the life and structure of DNA and RNA, and their 
function is incredibly important in the buildup and breakdown of cells.</p>
<p style='text-align:center'>
Our cells are carefully working together every day, and understanding what a nucleotide does can help us make sense 
of the basics of our cells and how they work.</p>
<h6 style='text-align: right; color: navy; '>Developed By: Jamiu Shaibu</h6>''', unsafe_allow_html=True)
