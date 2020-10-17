import numpy as np

def calculate(list):
    if len(list) != 9:
         raise ValueError('List must contain nine numbers.')
    else:
        array = np.array(list).reshape(3,3)

        mean = [(np.mean(array, axis=0)).tolist(), 
            (np.mean(array, axis=1)).tolist(), np.mean(list)]

        vari = [(np.var(array, axis=0)).tolist(), (
        np.var(array, axis=1)).tolist(), np.var(list)]

        std = [(np.std(array, axis=0)).tolist(), (
        np.std(array, axis=1)).tolist(), np.std(list)]

        maxi = [(np.max(array, axis=0)).tolist(), (
        np.max(array, axis=1)).tolist(), np.max(list)]

        minimum = [(np.min(array, axis=0)).tolist(), (
        np.min(array, axis=1)).tolist(), np.min(list)]

        total = [(np.sum(array, axis=0)).tolist(), (
        np.sum(array, axis=1)).tolist(), np.sum(list)]

        

        calculations = {
            'mean': mean,
            'variance': vari,
            'standard deviation': std,
            'max': maxi,
            'min': minimum,
            'sum': total,
        }
        calculations.update()
        



        return calculations
