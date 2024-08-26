class Transition_err(Exception):
      def __init__(self,previous,next_stage,message):
            self.previous = previous
            self.next_stage = next_stage
            self.message = message

      
