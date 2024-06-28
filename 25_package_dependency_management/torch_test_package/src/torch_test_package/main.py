import torch

def is_cuda():
    print(f'cuda.is_available: {torch.cuda.is_available()}')

def is_working():
    t = torch.rand(5, 3)
    print(t)
    print(f'shape: {t.shape}')
    print(f'dtype: {t.dtype}')
    print(f'device: {t.device}')


if __name__ == '__main__':
    is_cuda()
    is_working()
