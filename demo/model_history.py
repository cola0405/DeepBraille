from src.utils.BrailleProcessor import BrailleProcessor
import matplotlib.pyplot as plt


dp = BrailleProcessor('204.h5', 'index_value.txt')

dp.model.summary()

# print(history)
#
# plt.plot(history['acc'])
# plt.plot(history['val_acc'])
# plt.title("model accuracy")
# plt.ylabel("Accuracy")
# plt.xlabel("epoch")
# plt.legend(["train","test"],loc="lower right")
# plt.show()
