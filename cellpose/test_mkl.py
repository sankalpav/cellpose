import os, sys
os.environ["MKLDNN_VERBOSE"]="1"
import numpy as np
import mxnet as mx
import time
from cellpose.utils import use_gpu

def test_mkl():
    num_filter = 32
    kernel = (3, 3)
    pad = (1, 1)
    shape = (32, 32, 256, 256)

    x = mx.sym.Variable('x')
    w = mx.sym.Variable('w')
    y = mx.sym.Convolution(data=x, weight=w, num_filter=num_filter, kernel=kernel, no_bias=True, pad=pad)
    exe = y.simple_bind(mx.cpu(), x=shape)

    exe.arg_arrays[0][:] = np.random.normal(size=exe.arg_arrays[0].shape)
    exe.arg_arrays[1][:] = np.random.normal(size=exe.arg_arrays[1].shape)

    exe.forward(is_train=False)
    o = exe.outputs[0]
    t = o.asnumpy()
    
if __name__ == '__main__':
    test_mkl()
