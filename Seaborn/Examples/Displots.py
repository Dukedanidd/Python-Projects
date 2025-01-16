import seaborn as sns

pinguinos = sns.load_dataset('penguins')
print(pinguinos.head())

sns.displot(
    data = pinguinos,
    x = 'body_mass_g'
);