import monai.deploy.core as md
from gaussian_operator import GaussianOperator
from median_operator import MedianOperator
from sobel_operator import SobelOperator

from monai.deploy.core import Application


@md.resource(cpu=1)
@md.env(pip_packages=["scikit-image >= 0.17.2"])
class App(Application):
    def compose(self):
        sobel_op = SobelOperator()
        median_op = MedianOperator()
        gaussian_op = GaussianOperator()

        self.add_flow(sobel_op, median_op)
        self.add_flow(median_op, gaussian_op)

# Run the application when this file is executed.
if __name__ == "__main__":
    App(do_run=True)
