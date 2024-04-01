# Installation requirements

Need to install:

- npm
- yarn
- flask
- set the OPEN_AI_KEY environment variable

# Setup

We have the frontend in React (no UI framework yet). The `package.json` file has a `proxy` spec that fowards API requests to the react FE to the flask BE. This was modeled on this [youtube](https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project). To develop:

- run yarn commands from the `verbal-apt` directory
- start the flask BE in one terminal: `yarn start-api`
- start the react FE in another terminal: `yarn start`
- both the FE and BE should be getting hotloaded
