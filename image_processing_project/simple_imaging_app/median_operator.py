import monai.deploy.core as md
from monai.deploy.core import ExecutionContext, Image, InputContext, IOType, Operator, OutputContext, output


@md.input("image", Image, IOType.IN_MEMORY)
@md.output("image", Image, IOType.IN_MEMORY)
class MedianOperator(Operator):
    def compute(self, op_input: InputContext, op_output: OutputContext, context: ExecutionContext):
        from skimage.filters import median

        data_in = op_input.get().asnumpy()
        data_out = median(data_in)
        op_output.set(Image(data_out))
