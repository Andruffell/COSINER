from datasets import load_dataset
#https://huggingface.co/datasets/EMBO/BLURB/resolve/main/BLURB.py

ncbi = load_dataset("EMBO/BLURB", "NCBI-disease-IOB", trust_remote_code=True) #accessed Mar 17th 2025
chems = load_dataset("EMBO/BLURB", "BC5CDR-chem-IOB", trust_remote_code=True) #accessed Mar 17th 2025
genes = load_dataset("EMBO/BLURB", "BC2GM-IOB", trust_remote_code=True) #accessed Mar 17th 2025
bc5cdr_disease = load_dataset("EMBO/BLURB", "BC5CDR-disease-IOB", trust_remote_code=True) #accessed Mar 17th 2025
chemdner = load_dataset("jablonkagroup/chemdner", "raw_data", trust_remote_code=True) #accessed Mar 17th 2025
jnlpba = load_dataset("EMBO/BLURB", "JNLPBA", trust_remote_code=True) #accessed Mar 17th 2025

ncbi.save_to_disk("./data/ncbi.hf")
"""@article{10.5555/2772763.2772800,
          author = {Dogan, Rezarta Islamaj and Leaman, Robert and Lu, Zhiyong},
          title = {NCBI Disease Corpus},
          year = {2014},
          issue_date = {February 2014},
          publisher = {Elsevier Science},
          address = {San Diego, CA, USA},
          volume = {47},
          number = {C},
          issn = {1532-0464},
          abstract = {Graphical abstractDisplay Omitted NCBI disease corpus is built as a gold-standard resource for disease recognition.793 PubMed abstracts are annotated with disease mentions and concepts (MeSH/OMIM).14 Annotators produced high consistency level and inter-annotator agreement.Normalization benchmark results demonstrate the utility of the corpus.The corpus is publicly available to the community. Information encoded in natural language in biomedical literature publications is only useful if efficient and reliable ways of accessing and analyzing that information are available. Natural language processing and text mining tools are therefore essential for extracting valuable information, however, the development of powerful, highly effective tools to automatically detect central biomedical concepts such as diseases is conditional on the availability of annotated corpora.This paper presents the disease name and concept annotations of the NCBI disease corpus, a collection of 793 PubMed abstracts fully annotated at the mention and concept level to serve as a research resource for the biomedical natural language processing community. Each PubMed abstract was manually annotated by two annotators with disease mentions and their corresponding concepts in Medical Subject Headings (MeSH ) or Online Mendelian Inheritance in Man (OMIM ). Manual curation was performed using PubTator, which allowed the use of pre-annotations as a pre-step to manual annotations. Fourteen annotators were randomly paired and differing annotations were discussed for reaching a consensus in two annotation phases. In this setting, a high inter-annotator agreement was observed. Finally, all results were checked against annotations of the rest of the corpus to assure corpus-wide consistency.The public release of the NCBI disease corpus contains 6892 disease mentions, which are mapped to 790 unique disease concepts. Of these, 88% link to a MeSH identifier, while the rest contain an OMIM identifier. We were able to link 91% of the mentions to a single disease concept, while the rest are described as a combination of concepts. In order to help researchers use the corpus to design and test disease identification methods, we have prepared the corpus as training, testing and development sets. To demonstrate its utility, we conducted a benchmarking experiment where we compared three different knowledge-based disease normalization methods with a best performance in F-measure of 63.7%. These results show that the NCBI disease corpus has the potential to significantly improve the state-of-the-art in disease name recognition and normalization research, by providing a high-quality gold standard thus enabling the development of machine-learning based approaches for such tasks.The NCBI disease corpus, guidelines and other associated resources are available at: http://www.ncbi.nlm.nih.gov/CBBresearch/Dogan/DISEASE/.},
          journal = {J. of Biomedical Informatics},
          month = {feb},
          pages = {1–10},
          numpages = {10}}"""

chems.save_to_disk("./data/bc5cdr.hf")
"""@article{article,
          author = {Li, Jiao and Sun, Yueping and Johnson, Robin and Sciaky, Daniela and Wei, Chih-Hsuan and Leaman, Robert and Davis, Allan Peter and Mattingly, Carolyn and Wiegers, Thomas and lu, Zhiyong},
          year = {2016},
          month = {05},
          pages = {baw068},
          title = {BioCreative V CDR task corpus: a resource for chemical disease relation extraction},
          volume = {2016},
          journal = {Database},
          doi = {10.1093/database/baw068}
          }"""

genes.save_to_disk("./data/bc2gm.hf")
"""@article{article,
          author = {Smith, Larry and Tanabe, Lorraine and Ando, Rie and Kuo, Cheng-Ju and Chung, I-Fang and Hsu, Chun-Nan and Lin, Yu-Shi and Klinger, Roman and Friedrich, Christoph and Ganchev, Kuzman and Torii, Manabu and Liu, Hongfang and Haddow, Barry and Struble, Craig and Povinelli, Richard and Vlachos, Andreas and Baumgartner Jr, William and Hunter, Lawrence and Carpenter, Bob and Wilbur, W.},
          year = {2008},
          month = {09},
          pages = {S2},
          title = {Overview of BioCreative II gene mention recognition},
          volume = {9 Suppl 2},
          journal = {Genome biology},
          doi = {10.1186/gb-2008-9-s2-s2}
          }"""

bc5cdr_disease.save_to_disk("./data/bc5cdr_disease.hf")
"""@article{article,
          author = {Li, Jiao and Sun, Yueping and Johnson, Robin and Sciaky, Daniela and Wei, Chih-Hsuan and Leaman, Robert and Davis, Allan Peter and Mattingly, Carolyn and Wiegers, Thomas and lu, Zhiyong},
          year = {2016},
          month = {05},
          pages = {baw068},
          title = {BioCreative V CDR task corpus: a resource for chemical disease relation extraction},
          volume = {2016},
          journal = {Database},
          doi = {10.1093/database/baw068}
          }""",

chemdner.save_to_disk("./data/chemdner.hf")
"""@article{Krallinger2015,
  title        = {The CHEMDNER corpus of chemicals and drugs and its annotation principles},
  author       = {
    Krallinger, Martin and Rabal, Obdulia and Leitner, Florian and Vazquez,
    Miguel and Salgado, David and Lu, Zhiyong and Leaman, Robert and Lu, Yanan
    and Ji, Donghong and Lowe, Daniel M. and Sayle, Roger A. and
    Batista-Navarro, Riza Theresa and Rak, Rafal and Huber, Torsten and
    Rockt{"a}schel, Tim and Matos, S{'e}rgio and Campos, David and Tang,
    Buzhou and Xu, Hua and Munkhdalai, Tsendsuren and Ryu, Keun Ho and Ramanan,
    S. V. and Nathan, Senthil and {{Z}}itnik, Slavko and Bajec, Marko and
    Weber, Lutz and Irmer, Matthias and Akhondi, Saber A. and Kors, Jan A. and
    Xu, Shuo and An, Xin and Sikdar, Utpal Kumar and Ekbal, Asif and Yoshioka,
    Masaharu and Dieb, Thaer M. and Choi, Miji and Verspoor, Karin and Khabsa,
    Madian and Giles, C. Lee and Liu, Hongfang and Ravikumar, Komandur
    Elayavilli and Lamurias, Andre and Couto, Francisco M. and Dai, Hong-Jie
    and Tsai, Richard Tzong-Han and Ata, Caglar and Can, Tolga and Usi{'e},
    Anabel and Alves, Rui and Segura-Bedmar, Isabel and Mart{'i}nez, Paloma
    and Oyarzabal, Julen and Valencia, Alfonso
  },
  year         = 2015,
  month        = {Jan},
  day          = 19,
  journal      = {Journal of Cheminformatics},
  volume       = 7,
  number       = 1,
  pages        = {S2},
  doi          = {10.1186/1758-2946-7-S1-S2},
  issn         = {1758-2946},
  url          = {https://doi.org/10.1186/1758-2946-7-S1-S2},
  abstract     = {
    The automatic extraction of chemical information from text requires the
    recognition of chemical entity mentions as one of its key steps. When
    developing supervised named entity recognition (NER) systems, the
    availability of a large, manually annotated text corpus is desirable.
    Furthermore, large corpora permit the robust evaluation and comparison of
    different approaches that detect chemicals in documents. We present the
    CHEMDNER corpus, a collection of 10,000 PubMed abstracts that contain a
    total of 84,355 chemical entity mentions labeled manually by expert
    chemistry literature curators, following annotation guidelines specifically
    defined for this task. The abstracts of the CHEMDNER corpus were selected
    to be representative for all major chemical disciplines. Each of the
    chemical entity mentions was manually labeled according to its
    structure-associated chemical entity mention (SACEM) class: abbreviation,
    family, formula, identifier, multiple, systematic and trivial. The
    difficulty and consistency of tagging chemicals in text was measured using
    an agreement study between annotators, obtaining a percentage agreement of
    91. For a subset of the CHEMDNER corpus (the test set of 3,000 abstracts)
    we provide not only the Gold Standard manual annotations, but also mentions
    automatically detected by the 26 teams that participated in the BioCreative
    IV CHEMDNER chemical mention recognition task. In addition, we release the
    CHEMDNER silver standard corpus of automatically extracted mentions from
    17,000 randomly selected PubMed abstracts. A version of the CHEMDNER corpus
    in the BioC format has been generated as well. We propose a standard for
    required minimum information about entity annotations for the construction
    of domain specific corpora on chemical and drug entities. The CHEMDNER
    corpus and annotation guidelines are available at:
    ttp://www.biocreative.org/resources/biocreative-iv/chemdner-corpus/
  }
}"""

jnlpba.save_to_disk("./data/jnlpba.hf")
"""@inproceedings{collier-kim-2004-introduction,
          title = "Introduction to the Bio-entity Recognition Task at {JNLPBA}",
          author = "Collier, Nigel  and
            Kim, Jin-Dong",
          booktitle = "Proceedings of the International Joint Workshop on Natural Language Processing in Biomedicine and its Applications ({NLPBA}/{B}io{NLP})",
          month = aug # " 28th and 29th",
          year = "2004",
          address = "Geneva, Switzerland",
          publisher = "COLING",
          url = "https://aclanthology.org/W04-1213",
          pages = "73--78",
          }"""
