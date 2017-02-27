import math._
import scala.util._

/**
 * Grab Snaffles and try to throw them through the opponent's goal!
 * Move towards a Snaffle and use your team id to determine where you need to throw it.
 **/
object Player extends App {
    val myteamid = readInt // if 0 you need to score on the right of the map, if 1 you need to score on the left
    
    val wizard_array: Array[Wizard] = new Array[Wizard](2)
    val bludger_array: Array[Entity] = new Array[Entity](2)
    val opponent_array: Array[Entity] = new Array[Entity](2)
    val snaffle_target_array: Array[Snaffle] = new Array[Snaffle](2)

    var mana = 0
    var mana_garbage = 0
    var turn = 0            
    // game loop
    while(true) {
        
        val entities = readInt // number of entities still in game
        
        val num_snaffles = entities-6 
        val snaffle_array: Array[Snaffle]= new Array[Snaffle](num_snaffles)
        var num_snaffle = 0

        var seen_wizard = 0
        var seen_opponent = 0
        var seen_bludger = 0

        for(i <- 0 until entities) {
            // entityid: entity identifier
            // entitytype: "WIZARD", "OPPONENT_WIZARD" or "SNAFFLE" (or "BLUDGER" after first league)
            // x: position
            // y: position
            // vx: velocity
            // vy: velocity
            // state: 1 if the wizard is holding a Snaffle, 0 otherwise
            val Array(_entityid, entitytype, _x, _y, _vx, _vy, _state) = readLine split " "
            val entityid = _entityid.toInt
            val x = _x.toInt
            val y = _y.toInt
            val vx = _vx.toInt
            val vy = _vy.toInt
            val state = _state.toInt
            
            if (entitytype == "WIZARD" ){
                wizard_array(seen_wizard) = new Wizard(x, y , vx, vy, entityid, state, myteamid, seen_wizard, mana)
                seen_wizard+=1
            }
            else if (entitytype == "SNAFFLE"){
                snaffle_array(num_snaffle) = new Snaffle(x, y , vx, vy, entityid)
                num_snaffle += 1
            }
            else if (entitytype == "OPPONENT_WIZARD" ){
                opponent_array(seen_opponent) = new Entity(x, y , vx, vy, entityid)
                seen_opponent+=1
            }
            else if (entitytype == "BLUDGER"){
                bludger_array(seen_bludger) = new Bludger(x, y , vx, vy, entityid)
                seen_bludger += 1
            }
        }
        
        for(i <- 0 until 2) {
            snaffle_target_array(i) = wizard_array(i).find_target(snaffle_array,num_snaffles)
           
        }

         Console.err.println(snaffle_target_array(0).entityid, snaffle_target_array(1).entityid, num_snaffles>1 && snaffle_target_array(0).entityid == snaffle_target_array(1).entityid , wizard_array(0).squareDistance(snaffle_target_array(0))>wizard_array(1).squareDistance(snaffle_target_array(1)))
        
        // Check if the wizard have the same target
        if (num_snaffles>1 && snaffle_target_array(0).entityid == snaffle_target_array(1).entityid) {
            Console.err.println("change")
            val snaffle_opt_array: Array[Snaffle] = new Array[Snaffle](2)
            if (wizard_array(0).isAligned){
                snaffle_opt_array(1) = wizard_array(1).find_closest_except(snaffle_array,num_snaffles, snaffle_target_array(1).entityid)     
            }
            else if (wizard_array(0).isAligned){
                snaffle_opt_array(0) = wizard_array(0).find_closest_except(snaffle_array,num_snaffles, snaffle_target_array(0).entityid)                    
            }
            else {
                snaffle_opt_array(0) = wizard_array(0).find_closest_except(snaffle_array,num_snaffles, snaffle_target_array(0).entityid)                
                snaffle_opt_array(1) = wizard_array(1).find_closest_except(snaffle_array,num_snaffles, snaffle_target_array(1).entityid) 
                val dist_0 = wizard_array(0).squareDistance(snaffle_target_array(0)) + wizard_array(1).squareDistance(snaffle_opt_array(1))
                val dist_1 = wizard_array(1).squareDistance(snaffle_target_array(1)) + wizard_array(0).squareDistance(snaffle_opt_array(0))
                if (dist_0 > dist_1){
                    snaffle_target_array(0) = snaffle_opt_array(0)
                }
                else {
                    snaffle_target_array(1) = snaffle_opt_array(1)   
                }
            }

        }

        for(i <- 0 until 2) {
            // Write an action using println
            // To debug: Console.err.println("Debug messages...")
            
            // Edit this line to indicate the action for each wizard (0 ≤ thrust ≤ 150, 0 ≤ power ≤ 500)
            // i.e.: "MOVE x y thrust" or "THROW x y power"
         
            mana = wizard_array(i).play(snaffle_target_array(i), mana,num_snaffles)
            
        }
        
        turn+=1
        mana = min(mana+1, 100)
    }
}

class Point(var x: Float = 0, var y: Float = 0){

    def squareDistance(p: Point): Float = {
        (x-p.x)*(x-p.x)+(y-p.y)*(y-p.y)
    }
    def distance(p: Point): Double = {
        sqrt(squareDistance(p))
    }
}

class Entity(x: Float, y: Float, var vx: Int, var vy: Int, var entityid: Int) extends Point(x,y) {
   
    
    var isAligned = false

    
    def squareDistance(xa: Float, ya: Float, xb: Float, yb: Float): Float ={
        (xa-xb)*(xa-xb)+(ya-yb)*(ya-yb)
    }

    def squareDistanceEntityVitesse(e_1: Entity): Float ={
        squareDistance(x+vx, y+vy, e_1.x+e_1.vx, e_1.y+e_1.vy)
        
    }

    def find_closest(array_entity: Array[Entity], size: Int): Entity = {
        var squareDistance_closest_entity: Double = Double.PositiveInfinity
        var entity_target: Entity = array_entity(0)
        for(i <- 0 until size){
            var current_entity = array_entity(i)
            val current_squareDistance = squareDistanceEntityVitesse(current_entity)
            if (current_squareDistance < squareDistance_closest_entity) {
                squareDistance_closest_entity = current_squareDistance
                entity_target = current_entity
            }                   
        }
        return entity_target
    }
}

class Snaffle(x: Float, y: Float, vx: Int, vy: Int, entityid: Int) extends Entity(x,y,vx,vy,entityid) {
    def flipendo(wizard: Wizard){
       // var distance_wizard: Double = distance(wizard)
        var distance_wizard: Double = sqrt(squareDistanceEntityVitesse(wizard))
        if (distance_wizard == 0){
            var new_x  = x + vx
            var new_y  = y + vy
        }
        else {

            var radian = atan(((wizard.y +wizard.vy )-(y+vy))/((wizard.x +wizard.vx) -(x+vx)))
            var spell_power = min(6000 / (( distance_wizard / 1000 )*( distance_wizard / 1000 )), 1000 )
            var normalize_x = cos(radian) 
            var normalize_y = sin(radian) 
            var new_x = x + vx + 0.75*vx  + normalize_x * spell_power /0.5
            var new_y = y + vy + 0.75*vx + normalize_y * spell_power /0.5
            
            Console.err.println("1",  "x ", x+ vx  , "y ", y + vy, "angle " ,radian, cos(radian) , sin(radian))
            Console.err.println("2" , "x ", new_x  , "y ", new_y, "angle " ,radian, cos(radian) , sin(radian))
        }
    }

    def accio(wizard: Wizard){
       // var distance_wizard: Double = distance(wizard)
        var distance_wizard: Double = sqrt(squareDistanceEntityVitesse(wizard))
        if (distance_wizard == 0){
            var new_x  = x + vx
            var new_y  = y + vy
        }
        else {

            var radian = atan(((wizard.y +wizard.vy )-(y+vy))/((wizard.x +wizard.vx) -(x+vx)))
            var spell_power = min(3000 / (( distance_wizard / 1000 )*( distance_wizard / 1000 )), 1000 )
            var normalize_x = cos(radian) 
            var normalize_y = sin(radian) 
            var new_x = x + vx + 0.75*vx - normalize_x * spell_power / 0.5
            var new_y = y + vy + 0.75*vx - normalize_y * spell_power / 0.5
            
            Console.err.println("1",  "x ", x+ vx  , "y ", y + vy, "angle " ,radian, cos(radian) , sin(radian))
            Console.err.println("2" , "x ", new_x  , "y ", new_y, "angle " ,radian, cos(radian) , sin(radian))
        }
    }

    def action_throw(wizard: Wizard, target: Point){
        var radian = atan((wizard.y-(target.y-wizard.vy))/(wizard.x-(target.x-wizard.vx)))
        var new_vx = vx + cos(radian) * 500/0.5
        var new_vy = vy + sin(radian) * 500/0.5
        var new_x = x + new_vx
        var new_y= y + new_vy
        Console.err.println("x ", x+ new_vx  , "y ", y + new_vy, "angle " ,radian, cos(radian) , sin(radian))
        
    }

}

class Bludger(x: Float, y: Float, vx: Int, vy: Int, entityid: Int) extends Entity(x,y,vx,vy,entityid) 


class Wizard(x: Float, y: Float, vx: Int, vy: Int, entityid: Int, var state: Int,  val teamId: Int, val num: Int, var mana: Int) extends Entity(x,y,vx,vy,entityid) {
    var goal_center_x = 16000
    var goal_center_y = 3750

    if (teamId == 1){
        goal_center_x = 0
        
    }
    
    val goal_center = new Point(goal_center_x,goal_center_y)
    
    def action_throw(snaffle: Snaffle, target: Point){
        snaffle.action_throw(this, target)
    }
    
    def action_flipendo(snaffle: Snaffle){
        snaffle.flipendo(this)
    }
    
    def action_accio(snaffle: Snaffle){
        snaffle.accio(this)
    }

    def find_closest_except(array_entity: Array[Snaffle], size: Int, remove_id: Int): Snaffle = {
        var squareDistance_closest_entity: Double = Double.PositiveInfinity
        var entity_target: Snaffle = array_entity(0)
        for(i <- 0 until size){
            var current_entity = array_entity(i)
            val current_squareDistance = squareDistanceEntityVitesse(current_entity)
            
            if (current_squareDistance < squareDistance_closest_entity && current_entity.entityid != remove_id) {
                squareDistance_closest_entity = current_squareDistance
                entity_target = current_entity
            }            
           
        }
        return entity_target
    }
    
    def find_target(array_entity: Array[Snaffle], size: Int): Snaffle= {
        var squareDistance_closest_entity: Double = Double.PositiveInfinity
        isAligned = false
        var entity_target: Snaffle = array_entity(0)
        for(i <- 0 until size){
            var current_entity = array_entity(i)
            val current_squareDistance = squareDistanceEntityVitesse(current_entity)
            var slope: Float = 0
            var destinationY: Float = 0
            var s_x = current_entity.x
            var s_y = current_entity.y
            var s_vx = current_entity.vx
            var s_vy = current_entity.vy
            var dx: Float = (s_x) - (x)
            var dy: Float = (s_y) - (y)
            if (dx != 0 && mana>=20){
                slope = dy/dx
                destinationY = (s_y) + (goal_center_x - (s_x)) * slope
                var temp_isAligned = abs(destinationY - goal_center_y) < 2000 - 300
                if (temp_isAligned  && current_squareDistance < squareDistance_closest_entity){
                    if ((s_x > x && teamId == 0) || (s_x < x && teamId == 1)) {
                        entity_target = current_entity
                        squareDistance_closest_entity = current_squareDistance
                  //      Console.err.println("al",isAligned,num, current_entity.entityid,destinationY,slope)
                        isAligned = true
                    }
                
                    else {
                        isAligned = false
                     //Console.err.println("notal",isAligned,num, current_entity.entityid , destinationY,current_squareDistance)                                
                    }
                }
            }
     
            if (current_squareDistance < squareDistance_closest_entity && !isAligned) {
                squareDistance_closest_entity = current_squareDistance
                entity_target = current_entity
                //Console.err.println("clos",isAligned,num, current_entity.entityid , destinationY,current_squareDistance)
            }                   
        }
        return entity_target
    }


    def play(snaffle: Snaffle, mana_t: Int, num_snaffles: Int): Int = {
        
        
        var snaffle_x = snaffle.x.toInt
        var snaffle_y = snaffle.y.toInt 
        var snaffle_vx = snaffle.vx.toInt
        var snaffle_vy = snaffle.vy.toInt
        var snaffle_id =  snaffle.entityid.toInt
        Console.err.println("play", num , snaffle_id, isAligned, mana)
        
        mana = mana_t
        if (state == 1){ 
            action_throw(snaffle, goal_center)
                    
            println("THROW "+ (goal_center_x-vx).toString + " " + (goal_center_y-vy).toString + " 500")
        }
        
        else if (mana>=20 && snaffle_x+snaffle_vx < x +vx && teamId == 1 && isAligned) {
            println("FLIPENDO "+ snaffle_id)
            mana -= 20
        }
        else if (mana>=20 && snaffle_x+snaffle_vx > x+vx && teamId == 0 && isAligned) {
            action_flipendo(snaffle)
            println("FLIPENDO "+ snaffle_id)
            mana -= 20
        }
        else if (mana>=10 && num_snaffles>=1 &&  abs(snaffle_y+2*snaffle_vy-goal_center_y)<1000 && ( (snaffle_x+2*snaffle_vx <0 && teamId == 0) || (snaffle_x+2*snaffle_vx > 16000 && teamId == 1))){
            println("PETRIFICUS "+ snaffle_id)
        }
        
        else if (mana>=20 && snaffle_x+snaffle_vx < x + vx && teamId == 0 && squareDistanceEntityVitesse(snaffle)>3000000){
            action_accio(snaffle)
            println("ACCIO "+ snaffle_id)
            mana -= 20                
        }
        else if(mana>=20 && snaffle_x+snaffle_vx>x+vx && teamId == 1 && squareDistanceEntityVitesse(snaffle)>3000000) {
            println("ACCIO "+ snaffle_id)
            mana -= 20
        }
        else {            
            println("MOVE "+ (snaffle_x+snaffle_vx-vx).toString + " " + (snaffle_y+snaffle_vy-vy).toString + " 150")   
        }
        
        return mana   
    }
}
    


