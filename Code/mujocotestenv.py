import mujoco
import mujoco.viewer

path = r'.\MujocoEnvs\\'
#model_name=r'acrobot.xml'
#model_name=r'pend.xml'
#model_name=r'springball.xml'
# model_name=r'springmass.xml'
# model_name=r'cartpole.xml'
# model_name=r'halfcheetah.xml'
# model_name=r'quadant.xml'
# model_name=r'ballincup.xml'
model = mujoco.MjModel.from_xml_path(path + model_name)
data = mujoco.MjData(model)

# create the viewer object
viewer = mujoco.viewer.launch(model, data)

viewer.close()
