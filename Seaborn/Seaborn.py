import seaborn as sns
import matplotlib.pyplot as plt
propinas = sns.load_dataset('tips')

sns.relplot(
    data = propinas,
    x = 'total_bill',
    y = 'tip',
    hue = 'sex',
    style = 'smoker',
    size = 'size'
);

plt.show()