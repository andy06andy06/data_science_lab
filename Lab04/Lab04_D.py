import numpy as np
import matplotlib.pyplot as plt


def transition_matrix(n):
    P = []
    # TODO_D1
    prob_a = [0.6, 0.35, 0.05]
    prob_b = [0.5, 0.4, 0.1]
    if n==2:
        P = np.array([(0.4, 0.6),(0.5, 0.5)])
    else:
        P1 = np.diagflat([[prob_a[0]]*int((n+1)/2)+[prob_b[0]]*int((n-2)/2)],k=1)
        P2 = np.diagflat([prob_a[1]+prob_a[2]]+[0]*(n-2)+[prob_b[0]])
        P3 = np.diagflat([[prob_a[1]+prob_a[2]]+[prob_a[1]]*int((n-3)/2)+[prob_b[1]]*int((n/2))],k=-1)
        P = P1+P2+P3
        P[2:int((n+1)/2),0] = prob_a[2]
        P[int((n+1)/2):n,0] = prob_b[2]
    return P

def propagate(x0, P, k):
    xk = None
    # TODO_D2
    for i in range(k):
        x0 = np.dot(x0, P)
    xk = x0
    return xk

def create_sample(s0, P, k):
    trajectories = np.zeros(k)
    # TODO_D6
    temp = s0
    for i in range(k):
        trajectories[i] = temp
        temp = np.random.choice(a=P.shape[0],size=1,p=P[temp].flatten())
    
    return trajectories

def plot_distribution(x):
    plt.plot(x)
    plt.xticks(np.arange(0, len(x), step=1))
    plt.ylim(0, max(x)+0.1)
    plt.xlabel('State (i)')
    plt.ylabel('Probability')
    plt.title('Probability Distribution')
    plt.savefig('Lab04_D3.png', dpi=150)

def plot_histogram(x):
    plt.show()
    plt.hist(x, bins=int(max(x)+1), range=(-0.5, max(x)+0.5))
    plt.xticks(np.arange(0, max(x)+1, step=1))
    plt.xlabel('State (i)')
    plt.ylabel('Number of sample')
    plt.title('State Histogram')
    plt.savefig('Lab04_D7.png', dpi=150)
    
def main():
    
    P = transition_matrix(n=10)
    # TODO_D3
    x0 = [1,0,0,0,0,0,0,0,0,0]
    x10 = propagate(x0, P, k=8)
    plot_distribution(x10)
    
    # D4
    i = 1
    while x10[9]<0.01:
        i+=1
        x10 = propagate(x0, P, k=i)
    # print('It needs',i,'steps to be at least 0.01')

    # D5
    rand_x0 = np.random.dirichlet(np.ones(10),size=1)
    rand_x10 = propagate(rand_x0, P, k=1000)
    # print(x10)
    # print(rand_x10)

    # D7
    last_steps = []
    for i in range(1000):
        sample = create_sample(0,P,k=8)
        last_steps.append(sample[-1])
    plot_histogram(last_steps)

if __name__ == "__main__":
    main()