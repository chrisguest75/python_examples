import pprint
import torch
import importlib.metadata

def is_cuda():
    out = []
    out.append(f'cuda.is_available: {torch.cuda.is_available()}')
    out.append(f'importlib.metadata.version("torch"): {importlib.metadata.version("torch")}')
    pprint.pp(out)
    return out 

def is_working():
    out = []
    t = torch.rand(5, 3)
    out.append(str(t))
    out.append(f'shape: {t.shape}')
    out.append(f'dtype: {t.dtype}')
    out.append(f'device: {t.device}')
    pprint.pp(out)
    return out 

if __name__ == '__main__':
    is_cuda()
    is_working()
