// External Dependancies
const mongoose = require('mongoose');

const bdSchema = new mongoose.Schema({ id: String}, { strict: false});

module.exports = mongoose.model('BuildingDescription', bdSchema);