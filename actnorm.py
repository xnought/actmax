import torch


def actnorm(X: torch.Tensor, activation=torch.relu, alpha=1, dim=-1):
    act = activation(X)
    return act / (torch.sum(act, dim, keepdim=True) + alpha)
