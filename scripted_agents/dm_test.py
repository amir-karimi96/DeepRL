import functools

from absl import app
from absl import flags
from dm_control import manipulation

from dm_control import viewer

flags.DEFINE_enum(
    'environment_name', None, manipulation.ALL,
    'Optional name of an environment to load. If unspecified '
    'a prompt will appear to select one.')
FLAGS = flags.FLAGS


# TODO(b/121187817): Consolidate with dm_control/suite/explore.py
def prompt_environment_name(prompt, values):
  environment_name = None
  while not environment_name:
    environment_name = input(prompt)
    if not environment_name or values.index(environment_name) < 0:
      print('"%s" is not a valid environment name.' % environment_name)
      environment_name = None
  return environment_name


def main(argv):
  del argv
  environment_name = FLAGS.environment_name

  all_names = list(manipulation.ALL)

  if environment_name is None:
    print('\n  '.join(['Available environments:'] + all_names))
    environment_name = prompt_environment_name(
        'Please select an environment name: ', all_names)

  loader = functools.partial(
      manipulation.load, environment_name=environment_name)
  viewer.launch(loader)


if __name__ == '__main__':
  app.run(main)
