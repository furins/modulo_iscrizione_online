
import Vue from "vue";

const versionModule = {
    version: '1.0.33',
};
export default ({ Vue }) => {
    Vue.prototype.$application_built = versionModule;
}