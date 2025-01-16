import seaborn as sns

propinas = sns.load_dataset('tips')

sns.relplot(
    data = propinas,
    x = 'Total bill',
    y = 'Tip',
    hue = 'Sex',
    style = 'Smoker',
    size = 'Size'
);
# Seaborn se encarga de crear el grafico mas adeciado para mostrar la informacion