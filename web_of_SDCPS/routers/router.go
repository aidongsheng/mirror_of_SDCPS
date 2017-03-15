package routers

import (
	"flora_of_china/web_of_SDCPS/controllers"
	"github.com/astaxie/beego"
)

func init() {
    beego.Router("/", &controllers.MainController{})
}
